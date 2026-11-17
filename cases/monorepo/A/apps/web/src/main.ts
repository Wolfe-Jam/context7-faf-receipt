import { formatPrice } from '@acme/shared';

const el = document.querySelector('#price');
if (el) el.textContent = formatPrice(1999, 'EUR');
