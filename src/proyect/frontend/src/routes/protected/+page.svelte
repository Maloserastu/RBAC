<script lang="ts">
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  let username = '';
  let loading = true;

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

  function handleLogout() {
    localStorage.removeItem('token'); // Borra el token
    goto('/login'); // Redirige al login
  }

  //Navegación a otras secciones  (SOLO GESTION ACTIVA POR AHORA)
  function goToReto() {
    goto('/reto');
  }

  function goToGestion() {
    goto('/gestion');
  }

  function goToPerfil() {
    goto('/perfil');
  }
</script>

<!-- Imagenes de fondo y titulo-->
<img src={favicon2} alt="favicon" class="favicon2">
<p class="title">Remember It!?</p>
<img src={background} alt="background" class="fondo">


<div class="message">
{#if loading}
  <p>Cargando...</p>
{:else}
  <h1 class="bienvenida">Bienvenido, {username}</h1>
  <button on:click={handleLogout} class="logout-button">Cerrar sesión</button>
{/if}
  <div class="menu">
      <p class="titulo-protected">Selecciona una opción:</p>
      <button on:click={goToReto} >Reto diario</button>
      <button on:click={goToGestion}>Gestión</button>
      <button on:click={goToPerfil}>Perfil</button>
  </div>

</div>

<style>

/*Css global(body)*/

    :global(body){
        padding: 0px;
        margin: 0px;
        background-color: rgba(53, 134, 134, 0.33);
        overflow: hidden; /* <-- evita scroll vertical */
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
    
    
    /*Menu de selección*/
    .menu{
        display: flex;
        flex-direction: column;
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
        border: 3px solid white;    
        
    }
    .menu p{
      margin: auto;
      font: large;
      font-weight: bold;
      font-family: 'Courier New', Courier, monospace;
    }
   
    .menu button{
      margin: 15px;
      cursor: pointer;

      border: none;
      font-size: large;
      background: white;
      color: teal;
      border-radius: 10px;
      width: auto;
      padding: 3px;
      height: 25px;
      text-align: center; 
      border: 2px solid black;
      padding: 1px; 
    }


      .message {
      display: fixed;
      justify-content: center; 
      align-items: center;     
      height: 100vh;           
      flex-direction: column;  
    }
      .bienvenida{
        color: teal;
        position: fixed; 
        top: 100px;
        left: 600px;
        font-size: xx-large;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bolder;
        
      }
      .logout-button{
        position: fixed;
        bottom: 190px;
        right: 660px;
        font-size: large;
        background: none;
        color: white;
        border-radius: 10px;
        width: auto;
        border: solid 1px white;
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
    .titulo-protected{
      color: white;
      font-family: 'Courier New', Courier, monospace ;
    }
    

</style>