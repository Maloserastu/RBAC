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
<div class="message">
{#if loading}
  <p>Cargando...</p>
{:else}
  <h1>Bienvenido, {username}</h1>
  <button on:click={handleLogout}>Cerrar sesión</button>
{/if}
</div>

<style>

/*Css global(body)*/

    :global(body){
        padding: 0px;
        margin: 0px;
        background-color: rgba(53, 134, 134, 0.33);
    }

    /*Mensaje de inicio*/
    p,h1{
      font-family: 'Courier New', Courier, monospace;
      font-size: large;
    }

    button{
      background-color: rgba(75, 82, 175, 0.66);
      font-family: 'Courier New', Courier, monospace;
      font-weight: bold;
      border: 3px solid black;
      padding: 5px  30px;
    }
    .message {
      display: flex;
      justify-content: center; 
      align-items: center;     
      height: 100vh;           
      flex-direction: column;  
    }


</style>