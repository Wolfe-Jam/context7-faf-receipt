import { Button } from '@shop/ui';

export function Settings() {
  return (
    <section>
      <h1>Settings</h1>
      <Button onClick={() => alert('saved')}>Save</Button>
    </section>
  );
}
