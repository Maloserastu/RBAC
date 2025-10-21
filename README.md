Login personalizado con SvelteKit y FastApi en Python




Sobre la app

Este repositorio proporciona una creación de un login simple usando Python + FastApi para el backend y SvelteKit para el frontend.

Que esperar?

-La aplicación consta de un /login, /register y  /protected, siendo /protected una ruta segura a la que solo tendrán acceso los usuarios una vez inicien sesión.

-Seguridad controlada con una contraseña con hash usando tokens para controlar el acceso.

-Campos seguros y buenas prácticas como impedimento de duplicación de números de teléfono, nombres o gmail, junto con la prohibición de rellenar este último campo con algo que no se corresponda a un formato email.

-Tests con pytest sobre las funciones básicas CRUD de la app que se ejecutan sobre una base de datos secundaria.

Como funciona?

El frontend de SvelteKit se conecta al backend de Visual Studio Code(Python + FastApi). Este valida los datos, corre el código necesario y crea la base de datos en Docker Desktop con PostgreSQL si la app aún no se había ejecutado anteriormente en el dispositivo.

¡Aviso!

Este repositorio está creado por un programador junior y no ha sido revisado y testeado al 100% por lo que podría dar errores no registrados, tomados en cuenta y provocar bugs o roturas en la app imprevisibles. Descargar bajo vuestra propia responsabilidad!

Instalación


⭐Opcional:

La única tecnología que se ha usado y se recomienda usar  en el repositorio es WSL, pero se recomienda usarla. Su instalación no depende de otras tecnologías por lo que mostraré aquí los pasos necesarios para instalarla y cualquiera persona que la quiera usar puede seguirlos en cualquier momento.

WSL se usa para crear un entorno virtual de Ubuntu, mas concretamente Ubuntu 22.04 en nuestro caso, el cual nos permitirá tener el proyecto aislado y usar los comandos de linux, IMPORTANTE! Tener en cuenta que si no se hace esta instalación el proceso “Obligatorio” de instalación puede complicarse por falta de compatibilidad.

1.Primer paso

-Abrimos la terminal, powershell si estamos en windows


Comando:
wsl --install -d Ubuntu-22.04

Este comando instala primero wsl y después la versión de ubuntu concreta que especificamos, si tenemos una version antigua de windows puede ser necesario instalar  primero wsl a parte con wsl –install y configurar alguna otra cosas. Si este es el caso hay documentación sobre como hacerlo online.

2.Segundo paso

-Reiniciamos el sistema
-Abrimos la aplicación que se llame Ubuntu desde la tecla windows

3.Tercer paso

-Rellenamos los campos de configuración de ubuntu que se nos piden: usuario y contraseña

4.Cuarto paso

Para finalizar podemos comprobar que este todo correctamente instalado haciendo:

sudo apt update
sudo apt upgrade -y

wsl –version


🛡️Obligatorio:

Para problemas de compatibilidad consultar los pasos opcionales⬆️⬆️⬆️

💡Visual Studio Code

Se necesita tener Visual Studio instalado en el sistema. Este es el IDE con el que trabajaremos ya que facilita bastante el uso de varias de las otras tecnologías usadas en el desarrollo de esta aplicación.

Para descargarlo es tan sencillo como ir a la página oficial y clicar en el link de instalación para nuestro sistema(x64 de windows en la mayoría de los casos) y seguir los pasos de instalación una vez descargado y ejecutado el archivo .exe.

Link:Visual Studio Code - Code Editing. Redefined

🐍Python

Es el lenguaje de programación que usaremos para el proyecto y necesitaremos tenerlo instalado en el equipo asegurándonos de tener la versión correcta.

sudo apt update
sudo apt install -y software-properties-common
sudo app-apt-repository ppa:deadsnakes/ppa -y


Añadimos el soporte de entornos virtuales:

sudo apt update
sudo apt install -y python3.13 python3.13-venv python3.13-dev

Ahora podríamos verificar que la versión de python que tenemos es la adecuada

python3.13 –version

Lo cual debería mostrar la versión 3.13.0, y con esto ya se podrian crear entornos virtuales de ubuntu. En los siguiente pasos instalaremos tambien poetry, por lo que explicare como crear el entorno desde poetry mas adelante.

Aviso!
Puede ser que al crear ubuntu de problemas de compatibilidad python, ya que nuestra versión de ubuntu trabajara con otra versión de python que no será la 3.13.0 posiblemente, pero esto se puede arreglar al abrir el entorno virtual especificando que se use la versión que queremos en concreto.

📚Poetry

El siguiente paso es instalar poetry, lo cual nos permitirá a su vez instalar fast api y uvicorn de forma mucho más sencilla.

-Sabiendo que tenemos la version 3.13.0 de python instalada previamente:

Descargamos y ejecutamos el instalador:

curl -sSL https://install.python-poetry.org | python3.13 -

Agregamos poetry al PATH para poder usarla desde cualquier lugar:

echo ‘export PATH=”$HOME/.local/bin:$PATH”’ >> ~/.bashrc
source ~/.bashrc

Y por último comprobamos que se haya instalado correctamente con poetry –version

Cosas a tener en cuenta

1.Primer punto
Para crear el entorno virtual desde poetry usar la version de python 3.13.0 para evitar problemas:

poetry env use python3.13

Y para iniciar el entorno :

poetry env activate activate

Nos devolvera un “source /url….” y tendremos que copiarlo todo y enviarlo como comando de nuevo para activar el entorno. Una vez hecho ya deberíamos poder ver el entorno en funcionamiento y nos debería mostrar un (nombre_proyecto-py3.13) a la izquierda de nuestro usuario de linux y rutas.

2.Segundo punto

Tendremos que añadir las dependencias de fastapi y uvicorn al proyecto, pero para ello primero tenemos que hacer un git clone del repositorio(consultar documentación de git para instalarlo si hace falta):

git clone https://github.com/Maloserastu/Remember-It-.git

Una vez tenemos el repositorio en nuestro equipo tenemos que instalar las dependencias necesarias para correrlo sin errores.



Instalamos las siguiente versiones concretamente para que no den problemas de compatibilidad:

pip install passlib==1.7.4 bcrypt==4.1.2

Nos aseguramos de que estén instalados correctamente:

pip show passlib bcrypt

Añadimos las dependencias de FastApi y uvicorn  a poetry:

poetry add fastapi
poetry add uvicorn




3. Tercer paso

Al acabar de añadir todas estas dependencias nos faltaran el orm(SQLAlchemy), docker(PostgreSQL).

Instalamos en poetry SQLAlchemy:

poetry add sqlalchemy

y instalamos el driver para la conexión a postgre mas adelante:

poetry add psycopg2-binary

Cualquier otra dependencia necesaria para la app simplemente necesitará(no debería) imports desde alguna librería, pero no debería ya dar problemas.

4.Cuarto paso

Instalar Docker Desktop desde el sitio web oficial y seguir la documentación para instalarlo de forma normal si hace falta. Solamente pedirá las credenciales del entorno virtual de ubuntu al iniciarlo para entrar.

5.Último paso

Por último, quedan por añadir las dependencias de svelte.

sudo apt update
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/ install.sh | bash

recargamos bash :

source ~/bashrc

nvm install –lts
node -v
npm -v

6-Correr app 🚀

Hecho esto solo queda usar los comandos respectivos de uvicorn para iniciar el backend con:

uvicorn ruta_proyecto:app –reload

y el frontend lo siguiente desde la carpeta “frontend” del proyecto:

npm run dev

Y listo!