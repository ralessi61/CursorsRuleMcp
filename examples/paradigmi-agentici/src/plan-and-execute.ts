// Plan and Execute: prima si crea il piano, poi si eseguono i passi
import { cercaDocumenti, LLM } from "./strumenti.js";

// Pianificatore simulato: restituisce un elenco di passi (uno per riga)
const pianificatore: LLM = () =>
  ["cerca: ferie", "cerca: smart working", "cerca: rimborso", "riassumi"].join("\n");

// Esecutore: svolge un singolo passo (qui senza LLM, solo tool)
function esegui(passo: string, risultati: string[]): string {
  if (passo.startsWith("cerca: ")) return cercaDocumenti(passo.replace("cerca: ", ""));
  if (passo === "riassumi") return "RIEPILOGO ONBOARDING:\n" + risultati.join("\n");
  return "passo sconosciuto";
}

const obiettivo = "Prepara un riepilogo per un nuovo assunto su ferie, smart working e rimborsi";
console.log(`Obiettivo: ${obiettivo}\n`);

// 1. Pianificazione (una sola chiamata al modello "grande")
const piano = pianificatore(obiettivo).split("\n");
console.log("Piano:", piano.map((p, i) => `\n  ${i + 1}. ${p}`).join(""), "\n");

// 2. Esecuzione passo per passo
const risultati: string[] = [];
for (const passo of piano) {
  const r = esegui(passo, risultati);
  console.log(`> ${passo}\n${r}\n`);
  risultati.push(r);
}
