<script lang="ts">
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  let username = '';
  let loading = true;
  let role = "";

  import background from '$lib/icons/background.png';
  import favicon2 from '$lib/icons/flaterig.webp';

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

  function goBack() {
    goto('/protected');
  }
</script>

<!-- Imagenes de fondo y titulo-->
<img src={favicon2} alt="favicon" class="favicon2">
<p class="title">Remember It!?</p>
<img src={background} alt="background" class="fondo">


{#if loading}
  <p class="loading">Cargando...</p>
{:else}
  <div class="gestion-container">
    <h1>Panel de gestión</h1>
    <p class="welcome">Bienvenido, <strong>{username}</strong> ({role})</p>

    <div class="actions">
      <div class="card">
        <h2>👤 Crear usuario</h2>
        <p>Permite al admin o manager añadir nuevos usuarios.</p>
        <button disabled={role === 'usuario'}>Ir al creador de usuarios</button>
      </div>

      <div class="card">
        <h2>📂 Crear categoría</h2>
        <p>Los managers pueden crear nuevas categorías personalizadas.</p>
        <button disabled={role === 'usuario'}>Ir al creador de categorías</button>
      </div>


    </div>

    <button class="back-btn" on:click={goBack}>⬅️ Volver</button>
  </div>
{/if}


<style> 
/*Css global(body)*/

    :global(body){
        padding: 0px;
        margin: 0px;
        background-color: rgba(53, 134, 134, 0.33);
        overflow: hidden; /* <-- evita scroll vertical */

    }


    div{

        text-align: center;
        padding: 30px;
        font-family: 'Courier New', Courier, monospace;        
        position:absolute;
        transform: translate(-50%, -50%);
        left: 50%;
        top: 50%;        
        width: auto;
        height: auto;  
        border-radius: 15px ;    
        
    } 
div button{
  background-color: rgba(75, 82, 175, 0.66);
  font-family: 'Courier New', Courier, monospace;
  font-weight: bold;
  border: 3px solid black;
  padding: 5px  30px;
}
/*Img fondo de pantalla*/
    .fondo{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%; 
      z-index: -1; /*La mandamos al fondo*/
    }
    
    .favicon2{
      width: 70px;
      height: 70px; 
      margin :10px;
      position: fixed;
      top: 0px;
      border-radius: 50%;
    }
/*Remember it!?*/
    .title{
      font-weight: bold;
      position: fixed;
      top: -10px;
      font-size: xx-large;
      left: 7%;
      font-family: 'Courier New', Courier, monospace;
      color: white;
    } 
    
 
    







</style>