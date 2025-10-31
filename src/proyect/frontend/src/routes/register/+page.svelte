<script lang="ts">
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  let username = '';
  let password = '';
  let email = '';
  let phone = '';
  let error = '';
  let role = '';
  //Imports imagenes
  import eyeIcon from '$lib/icons/eye.svg';
  import background from '$lib/icons/background.png';
  import favicon2 from '$lib/icons/flaterig.webp';
  import decorativo2 from '$lib/icons/decorativo2.png';


//Protección de la página
  onMount(async () => {
    const token = localStorage.getItem('token');
    if (!token) {
      goto('/login');
      return;
    }

    try {
      const response = await fetch('http://localhost:8000/protected-data', {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (response.status !== 200) {
        localStorage.removeItem('token');
        goto('/login');
        return;
      }

      const data = await response.json();
      role = data.rol;

      // Si es usuario base, lo echamos
      if (role === 'usuario') {
        alert('No tienes permiso para acceder al registro.');
        goto('/protected');
        return;
      }
    } catch (err) {
      console.error('Error verificando el acceso:', err);
      goto('/login');
    }
  });


  //Repeticion show password
  let showPassword= false;
  function togglePassword() {  //funcion para mostrar
    showPassword = !showPassword;
  }
  //Registro
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
  <!-- Imagenes de fondo y titulo-->
<img src={favicon2} alt="favicon" class="favicon2">
<p class="title">Remember It!?</p>



<img src={background} alt="background" class="fondo">

  <div>
    <img src={decorativo2} alt="bordes" class="decorativo2" >

    <form on:submit|preventDefault={handleRegister}>
      <h1 class="titulo-registro">Registro</h1>
      <input type="text" placeholder="Username" bind:value={username} required />
      <input type="email" placeholder="Email" bind:value={email} required />
      <input type="text" placeholder="Phone" bind:value={phone} required />
      <input type={showPassword ? "text" : "password"} placeholder="Password" bind:value={password} required />
      <!-- Botón con imagen para mostrar/ocultar contraseña -->

  <button type="button" on:click={togglePassword} class="bteye" >
    <img src={eyeIcon} alt="Mostrar contraseña" width="24" height="24" />
  </button>
      <input type={showPassword ? "text" : "password"} placeholder="RepeatPassword" bind:value={password} required />
      <!-- Botón con imagen para mostrar/ocultar contraseña -->

  <button type="button" on:click={togglePassword} class="bteye2" >
    <img src={eyeIcon} alt="Mostrar contraseña" width="24" height="24" />
  </button>
      <button type="submit" class="bt-register">Registrarse</button>
      <p class="text1">¿Ya tienes cuenta?<a href="/login " class="link1"> Inicia sesión</a></p>
      {#if error}<p style="color:red">{error}</p>{/if}
      <img src={decorativo2} alt="bordes" class="decorativo3" >

    </form>
  </div>
<style> 
    /*Css global(body)*/

    :global(body){
        padding: 0px;
        margin: 0px;
        background-color: rgba(85, 99, 99, 0.488);
        overflow: hidden; /* <-- evita scroll vertical */

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
    .titulo-registro{
      color: white;
    }

    .text1{
      font-weight: bold;
      font-family: 'Courier New', Courier, monospace;
      color: white;
      display: flex;
      flex-direction: column;
    }
    .link1{
      padding-top: 15px;
    }
    /*Bordes y decoraciones*/
    
  
    .decorativo2{
      position: relative;
      top: 150px;
      right: -20px;
      width: 500px;
      pointer-events: none; /*Evita que el botón interfiera con el input de contraseña*/

    }
    .decorativo3{
      position: relative;
      top: -150px;
      right: -20px;
      width: 500px;
      pointer-events: none; /*Evita que el botón interfiera con el input de contraseña*/

    }
    .bt-register{
      border: none;
      font-size: large;
      background: none;
      color: teal;
      border-radius: 10px;
      width: 150px;
      padding: 0%;
      height: 25px;
      text-align: center;
      cursor: pointer;

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

    /*Css formulario*/
    form {
  display: flex;
  flex-direction: column; 
  gap: 15px; 
  align-items: center; /* Centra horizontalmente */
}


form input{

  font-weight: bold;
  padding: 5px;
  font-size: large;
  border: 3px solid black;
}
form h1{
  font-size: 2em;
}
form p{
  font-family: 'Courier New', Courier, monospace;

}
form a{
  text-decoration: none;
  color: teal;
}



/*CSS ojo mostrar contraseña*/
/**style="background: none; border: none; cursor: pointer;"*/
.bteye{
  background: none;
  border: none;
  cursor:pointer;
  position: fixed;
  top: 50.5%;
  right: 25%;
}
.bteye2{
  background: none;
  border: none;
  cursor:pointer;
  position: fixed;
  top: 54.5%;
  right: 25%;
}
input[type="password"]::-ms-reveal,
input[type="password"]::-ms-clear {
  display: none;
}


</style>