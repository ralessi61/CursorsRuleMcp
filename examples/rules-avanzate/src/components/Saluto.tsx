// Componente di esempio: aprilo in Cursor per attivare la regola componenti-react.mdc
interface SalutoProps {
  nome: string;
}

export function Saluto({ nome }: SalutoProps) {
  return <p className="saluto">Ciao, {nome}!</p>;
}
