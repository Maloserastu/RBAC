<script lang="ts">// se usa TypeScript
  import { goto } from '$app/navigation'; //navegación entre rutas y variables
  let username = '';
  let password = '';
  let error = '';

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


<form on:submit|preventDefault={handleLogin}>  <!-- Evita que se recarge la pagina y llama a la funcion handlelogin-->
    <h1>Login</h1>
  <input type="text" placeholder="Username" bind:value={username} required />
  <input type="password" placeholder="Password" bind:value={password} required />
  <button type="submit">Entrar</button>
  <p>¿No tienes cuenta? <a href="/register">Registrarse</a></p>
</form>

{#if error}
  <p style="color:red">{error}</p>
{/if}


<style> 
    form{
        text-align: center;
        padding: 1px;
        border: 3px solid rgb(5, 5, 5);
        font-family: 'Courier New', Courier, monospace;
    }   

</style>
