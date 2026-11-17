export const SUPPORTED_CURRENCIES = ['USD', 'EUR', 'GBP', 'JPY'] as const;
export type Currency = (typeof SUPPORTED_CURRENCIES)[number];

export function formatPrice(cents: number, currency: Currency): string {
  return new Intl.NumberFormat('en', { style: 'currency', currency }).format(cents / 100);
}
