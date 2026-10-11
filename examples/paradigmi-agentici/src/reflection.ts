// Reflection: bozza -> critica -> revisione, per al massimo N iterazioni
import { cercaDocumenti, LLM } from "./strumenti.js";

const contesto = cercaDocumenti("ferie");

// Autore simulato: la prima bozza "inventa" e non cita la fonte
const autore: LLM = (prompt) =>
  prompt.includes("CRITICA:")
    ? "Hai diritto a 26 giorni di ferie all'anno [fonte: policy-ferie.md]."
    : "Hai diritto a 30 giorni di ferie e puoi prenderli quando vuoi.";

// Critico: controlla che la risposta citi una fonte e usi i numeri del contesto
function critico(bozza: string): string | null {
  const problemi: string[] = [];
  if (!bozza.includes("[fonte:")) problemi.push("manca la citazione della fonte");
  const numeri = bozza.match(/\d+/g) ?? [];
  for (const n of numeri) if (!contesto.includes(n)) problemi.push(`il numero ${n} non è nei documenti`);
  return problemi.length ? problemi.join("; ") : null; // null = approvata
}

const domanda = "Quanti giorni di ferie ho?";
let bozza = autore(`Domanda: ${domanda}\nContesto: ${contesto}`);
for (let i = 1; i <= 3; i++) {
  console.log(`Bozza ${i}: ${bozza}`);
  const critica = critico(bozza);
  if (!critica) { console.log("Critico: ✅ approvata"); break; }
  console.log(`Critico: ❌ ${critica}`);
  bozza = autore(`Domanda: ${domanda}\nBozza: ${bozza}\nCRITICA: ${critica}`);
}
