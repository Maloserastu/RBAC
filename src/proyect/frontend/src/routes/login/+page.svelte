<script lang="ts">// se usa TypeScript
  import { goto } from '$app/navigation'; //navegación entre rutas y variables
  let username = '';
  let password = '';
  let error = '';
  let showPassword = false; //contraseña comienza escondida


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

<!-- Formulario del login-->

<div>
<form on:submit|preventDefault={handleLogin}>  <!-- Evita que se recarge la pagina y llama a la funcion handlelogin-->
    <h1>Login</h1>
  <input type="text" placeholder="Username" bind:value={username} required />
  <input type={showPassword ? "text" : "password"} placeholder="Password" bind:value={password} required /> 
  <!--pregunta a la funcion mostrar contraseña si debe ser mostrada o no-->
  

    
  <button type="submit">Entrar</button>
  <p>¿No tienes cuenta? <a href="/register">Registrarse</a></p>
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
    }


    div{
      background-color: rgba(111, 111, 12, 0.218);
        text-align: center;
        padding: 30px;
        font-family: 'Courier New', Courier, monospace;        
        position:absolute;
        transform: translate(-50%, -50%);
        left: 50%;
        top: 50%;        
        border: 4px double rgb(5, 5, 5);
        width: auto;
        height: auto;      
        
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






</style>