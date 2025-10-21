# Login personalizado con SvelteKit y FastAPI en Python

## Sobre la app

Este repositorio proporciona una creación de un login simple usando **Python + FastAPI** para el backend y **SvelteKit** para el frontend.

## ¿Qué esperar?

- La aplicación consta de `/login`, `/register` y `/protected`, siendo `/protected` una ruta segura a la que solo tendrán acceso los usuarios una vez inicien sesión.
- Seguridad controlada con una contraseña con hash usando tokens para controlar el acceso.
- Campos seguros y buenas prácticas como impedimento de duplicación de números de teléfono, nombres o gmail, junto con la prohibición de rellenar este último campo con algo que no se corresponda a un formato email.
- Tests con `pytest` sobre las funciones básicas CRUD de la app que se ejecutan sobre una base de datos secundaria.

## ¿Cómo funciona?

El frontend de SvelteKit se conecta al backend de Visual Studio Code (Python + FastAPI). Este valida los datos, corre el código necesario y crea la base de datos en Docker Desktop con PostgreSQL si la app aún no se había ejecutado anteriormente en el dispositivo.

> ⚠️ **Aviso:** Este repositorio está creado por un programador junior y no ha sido revisado y testeado al 100%, por lo que podría dar errores no registrados y provocar bugs o roturas en la app imprevisibles. ¡Descargar bajo vuestra propia responsabilidad!

---

## Instalación

### ⭐ Opcional: WSL

La única tecnología que se ha usado y se recomienda usar en el repositorio es **WSL**. Su instalación no depende de otras tecnologías, por lo que mostraré aquí los pasos necesarios para instalarla. Cualquier persona que la quiera usar puede seguirlos en cualquier momento.

WSL se usa para crear un entorno virtual de Ubuntu, más concretamente **Ubuntu 22.04**, el cual nos permitirá tener el proyecto aislado y usar los comandos de Linux.

> ⚠️ **IMPORTANTE:** Tener en cuenta que si no se hace esta instalación, el proceso “Obligatorio” de instalación puede complicarse por falta de compatibilidad.

#### 1. Primer paso

Abrimos la terminal (PowerShell si estamos en Windows) y ejecutamos:
```bash
wsl --install -d Ubuntu-22.04
