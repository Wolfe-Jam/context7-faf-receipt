export type Recipe = { id: number; title: string; minutes: number };

export const recipes: Recipe[] = [
  { id: 1, title: 'Tomato soup', minutes: 30 },
  { id: 2, title: 'Pancakes', minutes: 20 },
  { id: 3, title: 'Lentil curry', minutes: 45 }
];

export function formatMinutes(m: number): string {
  return m < 60 ? `${m} min` : `${Math.floor(m / 60)} h ${m % 60} min`;
}
