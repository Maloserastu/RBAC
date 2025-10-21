🧩 Login personalizado con SvelteKit y FastApi en Python
📘 Sobre la app

Este repositorio proporciona la creación de un login simple usando Python + FastApi para el backend y SvelteKit para el frontend.

🤔 ¿Qué esperar?

La aplicación consta de /login, /register y /protected, siendo /protected una ruta segura a la que solo tendrán acceso los usuarios una vez inicien sesión.

Seguridad controlada con una contraseña con hash usando tokens para controlar el acceso.

Campos seguros y buenas prácticas como impedimento de duplicación de números de teléfono, nombres o Gmail, junto con la prohibición de rellenar este último campo con algo que no se corresponda a un formato email.

Tests con pytest sobre las funciones básicas CRUD de la app que se ejecutan sobre una base de datos secundaria.

⚙️ ¿Cómo funciona?

El frontend de SvelteKit se conecta al backend en Visual Studio Code (Python + FastApi).
Este valida los datos, corre el código necesario y crea la base de datos en Docker Desktop con PostgreSQL si la app aún no se había ejecutado anteriormente en el dispositivo.

⚠️ ¡Aviso!

Este repositorio está creado por un programador junior y no ha sido revisado ni testeado al 100%, por lo que podría dar errores no registrados y provocar bugs o roturas imprevisibles.
Descargar bajo vuestra propia responsabilidad.

🧰 Instalación
⭐ Opcional

La única tecnología que se ha usado (y se recomienda usar) en el repositorio es WSL.
Su instalación no depende de otras tecnologías, por lo que aquí se muestran los pasos necesarios.

WSL se usa para crear un entorno virtual de Ubuntu —concretamente Ubuntu 22.04— que nos permitirá tener el proyecto aislado y usar comandos de Linux.

⚠️ IMPORTANTE: si no se realiza esta instalación, el proceso “Obligatorio” puede complicarse por falta de compatibilidad.

1️⃣ Primer paso

Abrimos la terminal (PowerShell si estamos en Windows):

wsl --install -d Ubuntu-22.04


Este comando instala primero WSL y después la versión de Ubuntu concreta.
Si tienes una versión antigua de Windows, puede que necesites instalar WSL aparte con wsl --install.

2️⃣ Segundo paso

Reinicia el sistema

Abre la aplicación Ubuntu desde el menú de inicio

3️⃣ Tercer paso

Configura Ubuntu con usuario y contraseña cuando se te solicite.

4️⃣ Cuarto paso

Comprobamos que todo esté correctamente instalado:

sudo apt update
sudo apt upgrade -y
wsl --version

🛡️ Obligatorio

Para problemas de compatibilidad, consulta los pasos opcionales anteriores.

💡 Visual Studio Code

Necesitas tener Visual Studio Code instalado.
Es el IDE con el que trabajaremos, ya que facilita el uso de las demás tecnologías.

📥 Descargar Visual Studio Code

🐍 Python

Instalamos Python 3.13.0 y el soporte para entornos virtuales:

sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install -y python3.13 python3.13-venv python3.13-dev


Verificamos la versión:

python3.13 --version


Debe mostrar Python 3.13.0.

⚠️ Nota: puede haber conflictos si Ubuntu usa otra versión de Python. Asegúrate de especificar la versión 3.13.0 al crear el entorno virtual.

📚 Poetry

Instalamos Poetry para gestionar dependencias y entornos virtuales fácilmente:

curl -sSL https://install.python-poetry.org | python3.13 -
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc


Verificamos instalación:

poetry --version

Cosas a tener en cuenta
1️⃣ Crear entorno virtual con Python 3.13.0
poetry env use python3.13
poetry env activate


Si devuelve una ruta tipo source /url/..., copia y ejecútala para activar el entorno.
Deberías ver algo como (nombre_proyecto-py3.13) al inicio de la línea de comandos.

2️⃣ Añadir dependencias FastAPI y Uvicorn

Primero, clona el repositorio:

git clone https://github.com/Maloserastu/Remember-It-.git


Instala las dependencias necesarias:

pip install passlib==1.7.4 bcrypt==4.1.2
pip show passlib bcrypt
poetry add fastapi
poetry add uvicorn

3️⃣ Añadir ORM y PostgreSQL

Instalamos SQLAlchemy y el driver de PostgreSQL:

poetry add sqlalchemy
poetry add psycopg2-binary

4️⃣ Instalar Docker Desktop

Descárgalo desde la web oficial de Docker y sigue la documentación.
Al iniciar pedirá las credenciales del entorno de Ubuntu.

5️⃣ Instalar dependencias de Svelte
sudo apt update
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install --lts
node -v
npm -v

🚀 Correr la app
Backend (FastAPI)

Desde el entorno virtual:

uvicorn ruta_proyecto:app --reload

Frontend (SvelteKit)

Desde la carpeta frontend del proyecto:

npm run dev


✅ ¡Y listo!
Tu entorno estará completamente preparado para correr la aplicación FastAPI + SvelteKit.
