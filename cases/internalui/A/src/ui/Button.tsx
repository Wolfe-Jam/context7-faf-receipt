import type { ButtonHTMLAttributes } from 'react';

type Props = ButtonHTMLAttributes<HTMLButtonElement> & { tone?: 'default' | 'danger' };

export function Button({ tone = 'default', className = '', ...rest }: Props) {
  return <button className={`shop-btn shop-btn--${tone} ${className}`} {...rest} />;
}
