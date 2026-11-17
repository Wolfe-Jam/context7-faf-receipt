import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

export function listPosts() {
  return prisma.post.findMany({ orderBy: { createdAt: 'desc' } });
}
