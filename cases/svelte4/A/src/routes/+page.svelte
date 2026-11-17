<script lang="ts">
  import type { PageData } from './$types';
  export let data: PageData;
</script>

<h1>Team directory</h1>
<ul>
  {#each data.people as person (person.id)}
    <li>{person.name} — {person.team}</li>
  {/each}
</ul>
