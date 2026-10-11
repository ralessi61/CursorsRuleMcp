export function divide(a: number, b: number): number {
  if (b === 0) throw new Error("Cannot divide by zero");
  return a / b;
}

export async function fetchUser(id: number): Promise<{ id: number; name: string }> {
  const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
  if (!res.ok) throw new Error(`User ${id} not found`);
  return res.json();
}
