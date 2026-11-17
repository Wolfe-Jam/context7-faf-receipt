<script lang="ts">
  import { formatMinutes } from '#lib/recipes.js';

  let { data } = $props();
</script>

<h1>Recipe box</h1>
<ul>
  {#each data.recipes as recipe (recipe.id)}
    <li>{recipe.title} · {formatMinutes(recipe.minutes)}</li>
  {/each}
</ul>
