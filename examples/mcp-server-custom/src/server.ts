// Server MCP minimale che espone un tool "cerca_documenti"
// sui file Markdown della cartella ./documenti.
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { readdirSync, readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

// Cartella dei documenti (funziona sia da src/ con tsx sia da dist/ dopo la build)
const CARTELLA_DOCUMENTI = join(dirname(fileURLToPath(import.meta.url)), "..", "documenti");

// Carica tutti i .md in memoria: { nome, testo }
function caricaDocumenti() {
  return readdirSync(CARTELLA_DOCUMENTI)
    .filter((f) => f.endsWith(".md"))
    .map((nome) => ({ nome, testo: readFileSync(join(CARTELLA_DOCUMENTI, nome), "utf8") }));
}

// 1. Creiamo il server con nome e versione
const server = new McpServer({ name: "documenti-aziendali", version: "1.0.0" });

// 2. Registriamo un TOOL: il modello può chiamarlo passando una "query"
server.registerTool(
  "cerca_documenti",
  {
    title: "Cerca nei documenti aziendali",
    description: "Cerca una parola o frase nei documenti aziendali e restituisce le righe trovate con il nome del file sorgente.",
    inputSchema: { query: z.string().describe("Parole da cercare, es. 'ferie'") },
  },
  async ({ query }) => {
    const parole = query.toLowerCase().split(/\s+/).filter(Boolean);
    const risultati: string[] = [];
    for (const doc of caricaDocumenti()) {
      // Teniamo le righe che contengono almeno una delle parole cercate
      const righe = doc.testo.split("\n").filter((r) => parole.some((p) => r.toLowerCase().includes(p)));
      if (righe.length > 0) risultati.push(`[fonte: ${doc.nome}]\n${righe.join("\n")}`);
    }
    const testo = risultati.length > 0 ? risultati.join("\n\n") : "Nessun risultato: non trovato nei documenti.";
    return { content: [{ type: "text", text: testo }] };
  }
);

// 3. Registriamo una RESOURCE: ogni documento leggibile con URI doc://<nome>
server.registerResource(
  "documento",
  new ResourceTemplate("doc://{nome}", {
    list: async () => ({
      resources: caricaDocumenti().map((d) => ({ uri: `doc://${d.nome}`, name: d.nome, mimeType: "text/markdown" })),
    }),
  }),
  { title: "Documento aziendale", description: "Contenuto completo di un documento" },
  async (uri, { nome }) => ({
    contents: [{ uri: uri.href, text: readFileSync(join(CARTELLA_DOCUMENTI, String(nome)), "utf8") }],
  })
);

// 4. Colleghiamo il server a stdin/stdout: Cursor lo avvia come processo figlio
const transport = new StdioServerTransport();
await server.connect(transport);
// Attenzione: con stdio NON usare console.log (sporcherebbe il protocollo). Usa console.error.
console.error("Server MCP 'documenti-aziendali' avviato");
