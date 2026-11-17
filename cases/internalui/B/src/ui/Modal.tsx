import type { ReactNode } from 'react';

type Props = { open: boolean; title: string; onClose: () => void; children: ReactNode };

export function Modal({ open, title, onClose, children }: Props) {
  if (!open) return null;
  return (
    <div className="shop-modal" role="dialog" aria-modal="true" aria-label={title}>
      <h2>{title}</h2>
      {children}
      <button className="shop-modal__close" onClick={onClose} aria-label="Close">×</button>
    </div>
  );
}
