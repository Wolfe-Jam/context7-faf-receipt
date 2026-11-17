import { sql } from './db';

export type Bookmark = { id: number; url: string; title: string; created_at: Date };

export function listBookmarks() {
  return sql<Bookmark[]>`select id, url, title, created_at from bookmarks order by created_at desc`;
}
