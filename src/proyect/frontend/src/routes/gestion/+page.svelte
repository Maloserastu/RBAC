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
    <h1 class="message">Panel de gestión</h1>
    <p class="welcome">Bienvenido, <strong>{username}</strong> ({role})</p>

    <div class="container">
      <div class="card">
        <h2>Crear usuario</h2>
        <p>Permite al admin o manager añadir nuevos usuarios.</p>
        <button disabled={role === 'usuario'} on:click={()=> goto('/register')}>Ir al creador de usuarios</button>
      </div>

      <div class="card">
        <h2>Crear categoría</h2>
        <p>Los managers pueden crear nuevas categorías personalizadas.</p>
        <button disabled={role === 'usuario'}>Ir al creador de categorías</button>
      </div>


    </div>

    <button class="back-btn" on:click={goBack}> Volver</button>
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


    /*Div padre*/
    .gestion-container {
  padding: 20px;
  margin: 0 auto;
  width: 60%;
  min-height: 70vh;
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center; /* centra verticalmente el contenido */
  align-items: center;     /* centra horizontalmente */
  gap: 50px;
  
  position:absolute;
  transform: translate(-50%, -50%);
  left: 50%;
  top: 50%;     
}
/*Div hijo*/
.container {
  border: 3px solid rgb(148, 148, 139);
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  gap: 20px;
  width: 100%;
  height: 100%;
  padding: 20px;
  box-sizing: border-box;
  position: relative;
  align-items: center;
  
}
.gestion-container h2{
    color: white;
    font-family: 'Courier New', Courier, monospace;
    border-bottom: 1px solid white;
}
.gestion-container button{
    cursor: pointer;

}
    /*  Crear usuario-crear categoria   */
    .card{
        position: inherit;
        padding: 5%;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        gap: 15px;
        text-align: center;
    }
    /*Panel de gestion*/
    .message{
        font-family: 'Courier New', Courier, monospace;
        border-bottom: 1px solid white;
        width: 100%;
        text-align: center;
        padding-bottom: 1%;
        padding-top: 0%;
    }
    /*Bienvenido "name"*/
    .welcome{
        font-family: 'Courier New', Courier, monospace;
        font-size: large;
        padding-top: 0%;
        padding-bottom: 0%;
    }
    /*Volver*/
    .back-btn{
        border-radius: 15px ;    
        color: white;
        border: none;
        font-size: large;
        background: none;  
        cursor: pointer;
        border-radius: 10px;
        border: solid 1px white;      
    }
    /*Mensaje de cargando mientras no muestra los datos*/
    .loading{
        color: white;
        position: absolute ;
        font-size: xx-large;
        top: 45%;
        left: 45%;


    }
    
div button{
  background-color: rgba(68, 76, 80, 0.66);
  font-family: 'Courier New', Courier, monospace;
  font-weight: bold;
  border: 3px solid teal;
  padding: 5px  30px;
  border-radius: 15px;
  font-size: medium;
  text-align: center;
  color: white;
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