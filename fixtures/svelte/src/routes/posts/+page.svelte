<script lang="ts">
  import type { PageData } from './$types';

  let { data }: { data: PageData } = $props();
  let count = $derived(data.posts.length);
</script>

<h1>Posts ({count})</h1>
<ul>
  {#each data.posts as post (post.id)}
    <li>{post.title}</li>
  {/each}
</ul>
