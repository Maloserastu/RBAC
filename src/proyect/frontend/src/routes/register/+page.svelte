<script lang="ts">
  import { goto } from '$app/navigation';
  let username = '';
  let password = '';
  let email = '';
  let phone = '';
  let error = '';

  async function handleRegister() {
    error = '';
    try {
      const response = await fetch('http://localhost:8000/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password, email, phone })
      });

      if (!response.ok) {
        const data = await response.json();
        error = data.detail || 'Error en el registro';
        return;
      }

      // Si el registro es exitoso, redirige al login
      goto('/login');
    } catch (err) {
      error = 'Error de conexión con el servidor';
    }
  }
</script>

<form on:submit|preventDefault={handleRegister}>
  <h1>Registro</h1>
  <input type="text" placeholder="Username" bind:value={username} required />
  <input type="password" placeholder="Password" bind:value={password} required />
  <input type="email" placeholder="Email" bind:value={email} required />
  <input type="text" placeholder="Phone" bind:value={phone} required />
  <button type="submit">Registrarse</button>
  <p>¿Ya tienes cuenta?<a href="/login "> Inicia sesión</a></p>
  {#if error}<p style="color:red">{error}</p>{/if}
</form>