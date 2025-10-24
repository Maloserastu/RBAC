<script lang="ts">
  import { goto } from '$app/navigation';
  let username = '';
  let password = '';
  let email = '';
  let phone = '';
  let error = '';

  import eyeIcon from '$lib/icons/eye.svg';

  //Repeticion show password
  let showPassword= false;
  function togglePassword() {  //funcion para mostrar
    showPassword = !showPassword;
  }
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

  <div>
    <form on:submit|preventDefault={handleRegister}>
      <h1>Registro</h1>
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
      <button type="submit">Registrarse</button>
      <p>¿Ya tienes cuenta?<a href="/login "> Inicia sesión</a></p>
      {#if error}<p style="color:red">{error}</p>{/if}
    </form>
  </div>
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



/*CSS ojo mostrar contraseña*/
/**style="background: none; border: none; cursor: pointer;"*/
.bteye{
  background: none;
  border: none;
  cursor:pointer;
  position: fixed;
  top: 54%;
  right: 10%;
}
.bteye2{
  background: none;
  border: none;
  cursor:pointer;
  position: fixed;
  top: 64%;
  right: 10%;
}
input[type="password"]::-ms-reveal,
input[type="password"]::-ms-clear {
  display: none;
}


</style>