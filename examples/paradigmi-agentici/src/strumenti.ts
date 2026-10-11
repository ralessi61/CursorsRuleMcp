// Strumenti e LLM SIMULATI: nessuna API key necessaria.

// Piccolo "archivio documenti" in memoria
export const DOCUMENTI: Record<string, string> = {
  "policy-ferie.md": "Ogni dipendente ha diritto a 26 giorni di ferie all'anno.",
  "smart-working.md": "Smart working fino a 2 giorni a settimana.",
  "rimborsi-spese.md": "Rimborso massimo per un pasto in trasferta: 30 euro.",
};

// Tool: cerca una parola nei documenti e restituisce "[fonte] testo"
export function cercaDocumenti(query: string): string {
  const trovati = Object.entries(DOCUMENTI)
    .filter(([, testo]) => testo.toLowerCase().includes(query.toLowerCase()))
    .map(([nome, testo]) => `[fonte: ${nome}] ${testo}`);
  return trovati.length ? trovati.join("\n") : "non trovato nei documenti";
}

// Tool: calcolatrice semplice (solo numeri e + - * /)
export function calcola(espressione: string): string {
  if (!/^[\d\s+\-*/().]+$/.test(espressione)) return "espressione non valida";
  return String(Function(`return (${espressione})`)());
}

// "LLM" finto: riceve un prompt e restituisce una risposta scritta a mano
// in base a parole chiave. Serve solo a mostrare il flusso dei paradigmi.
export type LLM = (prompt: string) => string;
