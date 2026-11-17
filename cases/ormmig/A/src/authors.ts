import { eq } from 'drizzle-orm';
import { db } from './db';
import { authors } from './db/schema';

export function getAuthor(id: number) {
  return db.select().from(authors).where(eq(authors.id, id));
}
