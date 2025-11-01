<script lang="ts">// se usa TypeScript
  import { goto } from '$app/navigation'; //navegación entre rutas y variables
  let username = '';
  let password = '';
  let error = '';
  let showPassword = false; //contraseña comienza escondida

  import eyeIcon from '$lib/icons/eye.svg';
  import background from '$lib/icons/background.png';
  import favicon2 from '$lib/icons/flaterig.webp';
  import decorativo2 from '$lib/icons/decorativo2.png';


  function togglePassword() {  //funcion para mostrar
    showPassword = !showPassword;
  }


  async function handleLogin() {//funcion que se ejecuta al enviar el formulario, se inicia con "" para borrar mensajes anteriores
    error = '';
    try {
      const response = await fetch('http://localhost:8000/login', {//peticion POST al backend del login
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded' //Se cambia el tipo de dato para que lo acepte OAuth2PasswordRequestForm
        },
        body: new URLSearchParams({
          username,
          password
        })
      });
      //Captura el error si no devuelve 200 
      if (!response.ok) {
        const data = await response.json();
        error = data.detail || 'Error en el login';
        return;
      }
      //Si el login no falla, se guarda el token para mas adelante y redirige al protected

      const data = await response.json();
      localStorage.setItem('token', data.access_token);
      goto('/protected');
    } catch (err) { //Captura de errores mas generales
      error = 'Error de conexión con el servidor';
    }
  }
</script>
<!-- Imagenes de fondo y titulo-->
<img src={favicon2} alt="favicon" class="favicon2">
<p class="title">Remember It!?</p>
<img src={background} alt="background" class="fondo">



<!-- Formulario del login-->

<div>
  

<form on:submit|preventDefault={handleLogin}>  <!-- Evita que se recarge la pagina y llama a la funcion handlelogin-->
  <img src={decorativo2} alt="bordes" class="decorativo2" >
    <h1 class="titulo-login">Login</h1>
  <input type="text" placeholder="Username" bind:value={username} required />
  <input type={showPassword ? "text" : "password"} placeholder="Password" bind:value={password} required  /> 
  <!--pregunta a la funcion mostrar contraseña si debe ser mostrada o no-->
  
  
<!-- Botón con imagen para mostrar/ocultar contraseña -->

  <button type="button" on:click={togglePassword} class="bteye" >
    <img src={eyeIcon} alt="Mostrar contraseña" width="24" height="24" />
  </button>

  

    
  <button type="submit" class="bt-login">Entrar</button>
  <p class="text1">¿No tienes cuenta? <a href="/register" class="link1">Registrarse</a></p>
    <img src={decorativo2} alt="bordes" class="decorativo3" >

</form>
</div>
{#if error}
  <p style="color:red">{error}</p>
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
    .titulo-login{
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
      right: -25px;
      width: 500px;
      pointer-events: none; /*Evita que el botón interfiera con el input de contraseña*/

      
      

    }
    .decorativo3{
      position: relative;
      top: -150px;
      right: -25px;
      width: 500px;   
      pointer-events: none; /*Evita que el botón interfiera con el input de contraseña*/
 
    }
    .bt-login{
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

    /*Css formulario*/
    form {
  display: flex;
  flex-direction: column; 
  gap: 10px; 
  align-items: center; /* Centra horizontalmente */
}

form input{

  font-weight: bold;
  padding: 5px;
  font-size: large;
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
  top: 48.5%;
  right: 25%;
}
input[type="password"]::-ms-reveal,
input[type="password"]::-ms-clear {
  display: none;
}



</style>