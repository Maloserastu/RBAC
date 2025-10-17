<script lang="ts">
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  let username = '';
  let loading = true;

  onMount(async () => {
    try {
      const token = localStorage.getItem('token');
      if (!token) {
        goto('/login');
        return;
      }

      const response = await fetch('http://localhost:8000/protected-data', {
        headers: { Authorization: `Bearer ${token}` }
      });

      if (response.status === 401) {
        localStorage.removeItem('token');
        goto('/login');
        return;
      }

      const data = await response.json();
      username = data.username;
    } catch (err) {
      console.error('Error al cargar datos:', err);
    } finally {
      loading = false;
    }
  });

  function handleLogout() {
    localStorage.removeItem('token'); // ✅ Borra el token
    goto('/login'); // ✅ Redirige al login
  }
</script>

{#if loading}
  <p>Cargando...</p>
{:else}
  <h1>Bienvenido, {username}</h1>
  <button on:click={handleLogout}>Cerrar sesión</button>
{/if}