Sistema Modular de Configuración y Gestión de Usuarios
GA1-220501093-04-AA1-EV06 – Python avanzado
Entornos Virtuales, Gestión de Dependencias, Variables de Entorno y Modularización
1. Descripción del proyecto
El presente proyecto consiste en el desarrollo de un sistema modular de configuración y gestión de usuarios desarrollado en Python y ejecutado desde consola.

La aplicación permite registrar usuarios, listar usuarios registrados, buscar usuarios por nombre, validar los datos ingresados y mostrar la configuración de la aplicación mediante variables de entorno.

El proyecto fue desarrollado aplicando conceptos de Python avanzado como entornos virtuales, gestión de dependencias, variables de entorno, módulos, paquetes, importación de módulos y manejo de excepciones.

Este proyecto corresponde a la evidencia:

GA1-220501093-04-AA1-EV06 – Python avanzado: Entornos Virtuales, Gestión de Dependencias, Variables de Entorno y Modularización.

2. Objetivo
Desarrollar una aplicación modular en Python que permita gestionar usuarios desde consola aplicando buenas prácticas de organización y desarrollo de software.

Los principales conceptos aplicados son:

Creación y utilización de entornos virtuales.
Gestión de dependencias mediante pip.
Generación del archivo requirements.txt.
Uso de variables de entorno.
Utilización de python-dotenv.
Creación de módulos y paquetes.
Importación de módulos.
Separación de responsabilidades.
Validación de datos.
Manejo de excepciones.
Organización estructurada de un proyecto Python.
3. Tecnologías utilizadas
El proyecto fue desarrollado utilizando las siguientes tecnologías y herramientas:

Python 3.14.7
pip 26.2.1
python-dotenv 1.2.3
venv
Visual Studio Code
Git
GitHub
PowerShell
4. Funcionalidades del sistema
El sistema cuenta con un menú de opciones que permite realizar las siguientes operaciones:

Registrar usuarios.
Listar usuarios registrados.
Buscar usuarios por nombre.
Mostrar la configuración de la aplicación.
Salir del sistema.
También cuenta con validaciones para evitar errores en los datos ingresados.

Validaciones implementadas
Validación de nombres vacíos.
Validación de nombres con mínimo dos caracteres.
Validación de edades negativas.
Validación de edades superiores a 120 años.
Validación para evitar ingresar texto en el campo de edad.
Manejo de errores mediante excepciones.
5. Estructura del proyecto
sistema_usuarios/
│
├── .venv/
│
├── app/
│   ├── __init__.py
│   │
│   ├── usuarios/
│   │   ├── __init__.py
│   │   ├── gestor.py
│   │   └── validaciones.py
│   │
│   └── config/
│       ├── __init__.py
│       └── settings.py
├── capturas
├── .env
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
6. Descripción de los módulos
main.py

Es el punto de entrada principal de la aplicación.

Se encarga de:

Mostrar el menú principal. Recibir las opciones del usuario. Ejecutar las funciones correspondientes. Mostrar mensajes personalizados. Manejar excepciones. Coordinar los diferentes módulos del proyecto. app/usuarios/gestor.py

Contiene la clase GestorUsuarios.

Este módulo se encarga de administrar las operaciones relacionadas con los usuarios.

Sus principales funciones son:

Registrar usuarios. Listar usuarios. Buscar usuarios.

La información de los usuarios se administra durante la ejecución de la aplicación.

app/usuarios/validaciones.py

Contiene las funciones encargadas de validar los datos ingresados.

Entre las validaciones implementadas se encuentran:

Validar que el nombre no esté vacío. Validar que el nombre tenga al menos dos caracteres. Validar que la edad no sea negativa. Validar que la edad no sea superior a 120 años.

Cuando se encuentra un dato incorrecto se utiliza la excepción ValueError.

app/config/settings.py

Este módulo se encarga de cargar las variables de entorno utilizando la biblioteca python-dotenv.

Las variables utilizadas son:

APP_NAME APP_VERSION ADMIN_USER

Estas variables son utilizadas por el programa principal para mostrar información de configuración.

7. Entorno virtual
Para el desarrollo del proyecto se utilizó un entorno virtual creado mediante venv.

El entorno virtual permite aislar las dependencias del proyecto de las dependencias instaladas globalmente en el computador.

Crear el entorno virtual

El comando utilizado normalmente para crear el entorno es:

python -m venv .venv

Durante la configuración de este proyecto se presentó un inconveniente con la instalación automática de pip, por lo que se utilizó la siguiente alternativa:

python -m venv .venv --without-pip

Posteriormente se instaló pip utilizando:

python -m ensurepip --upgrade Activar el entorno virtual

En Windows PowerShell:

..venv\Scripts\Activate.ps1

Cuando el entorno se encuentra correctamente activado, la terminal muestra:

(.venv)

Por ejemplo:

(.venv) PS C:\Users\PABLO 08\OneDrive\Escritorio\sistema_usuarios>

8. Gestión de dependencias
El proyecto utiliza pip para administrar sus dependencias.

La principal dependencia utilizada es:

python-dotenv

Esta biblioteca permite cargar las variables almacenadas en el archivo .env.

La instalación se realizó mediante:

python -m pip install python-dotenv

La versión utilizada en el proyecto es:

python-dotenv==1.2.3

9. Archivo requirements.txt
El archivo requirements.txt permite registrar las dependencias necesarias para ejecutar el proyecto.

Actualmente contiene:

python-dotenv==1.2.3

Para generar el archivo a partir de las dependencias instaladas se utilizó:

python -m pip freeze > requirements.txt

Para instalar posteriormente todas las dependencias del proyecto se puede utilizar:

python -m pip install -r requirements.txt

10. Variables de entorno
El proyecto utiliza variables de entorno para separar la configuración del código fuente.

El archivo utilizado es:

.env

Su contenido es:

APP_NAME=Sistema Usuarios APP_VERSION=1.0 ADMIN_USER=admin

Estas variables son cargadas utilizando python-dotenv.

En el archivo settings.py se utiliza:

from dotenv import load_dotenv

y posteriormente:

load_dotenv()

Las variables son obtenidas mediante:

os.getenv()

11. Seguridad de las variables de entorno
El archivo .env contiene información de configuración y por esta razón no debe publicarse directamente en un repositorio público.

Para evitar que Git lo incluya, se agregó al archivo .gitignore:

.env

En cambio, el proyecto contiene:

.env.example

Este archivo funciona como plantilla y muestra las variables necesarias:

APP_NAME=Sistema Usuarios APP_VERSION=1.0 ADMIN_USER=admin

De esta manera, otra persona puede conocer qué variables necesita configurar sin tener que publicar el archivo .env.

12. Archivo .gitignore
El proyecto utiliza el siguiente archivo .gitignore:

.venv/ .env pycache/ *.pyc

Esto permite evitar que se suban al repositorio:

El entorno virtual. Las variables de entorno. Archivos temporales de Python. Archivos compilados de Python.

13. Ejecución del proyecto
Para ejecutar el proyecto se debe abrir una terminal dentro de la carpeta:

sistema_usuarios Paso 1. Activar el entorno virtual ..venv\Scripts\Activate.ps1 Paso 2. Verificar Python python --version

Resultado utilizado durante el desarrollo:

Python 3.14.7 Paso 3. Verificar pip python -m pip --version Paso 4. Instalar las dependencias python -m pip install -r requirements.txt Paso 5. Ejecutar la aplicación python main.py

14. Menú principal
Al ejecutar el programa se muestra el siguiente menú:

======================================== Sistema Usuarios - versión 1.0
Registrar usuario
Listar usuarios
Buscar usuario
Mostrar configuración
Salir
Seleccione una opción:

15. Registro de usuarios
Para registrar un usuario se selecciona la opción:

1

Posteriormente el sistema solicita:

Ingrese el nombre: Ingrese la edad:

Por ejemplo:

Ingrese el nombre: Pablo Ingrese la edad: 25

El sistema muestra:

Usuario registrado correctamente: Pablo (25 años)

16. Listado de usuarios
Para visualizar los usuarios registrados se selecciona:

2

El sistema muestra los usuarios registrados durante la ejecución:

Usuarios registrados:

Pablo - 25 años
17. Búsqueda de usuarios
Para buscar un usuario se selecciona:

3

Después se introduce el nombre:

Ingrese el nombre que desea buscar: Pablo

Si el usuario existe, el sistema muestra:

Usuario encontrado: Pablo - 25 años

Si no existe:

No se encontró el usuario.

18. Visualización de configuración
La opción:

4

permite comprobar que las variables de entorno están funcionando correctamente.

El resultado es:

Configuración del sistema Nombre de la aplicación: Sistema Usuarios Versión: 1.0 Usuario administrador: admin

Esto demuestra que la aplicación está leyendo correctamente la información almacenada en .env.

19. Validación de nombre vacío
El sistema evita registrar usuarios sin nombre.

Si el usuario deja el campo vacío:

Ingrese el nombre:

se muestra:

Error: El nombre no puede estar vacío.

20. Validación de edad negativa
Si se introduce una edad negativa:

Ingrese la edad: -5

el sistema muestra:

Error: La edad no puede ser negativa.

21. Validación de edad superior a 120
Si se introduce:

Ingrese la edad: 150

el sistema muestra:

Error: La edad ingresada no es válida.

22. Validación de edad no numérica
El sistema también controla cuando el usuario introduce letras en lugar de un número.

Por ejemplo:

Ingrese la edad: abc

El sistema muestra:

Error: La edad debe ser un número entero.

Esto permite evitar que el programa termine inesperadamente debido a una entrada incorrecta.

23. Manejo de excepciones
El proyecto utiliza excepciones para controlar errores durante la ejecución.

Una de las excepciones principales utilizadas es:

ValueError

El bloque try/except permite capturar errores y mostrar mensajes comprensibles para el usuario.

Esto mejora la experiencia de uso y evita que la aplicación se cierre inesperadamente cuando se ingresan datos incorrectos.

24. Modularización
La aplicación fue dividida en diferentes módulos para separar responsabilidades.

La organización principal es:

main.py │ ├── app.config.settings │ └── app.usuarios.gestor │ └── app.usuarios.validaciones

De esta manera, cada módulo tiene una responsabilidad específica.

Ventajas encontradas

La modularización permite:

Organizar mejor el código. Facilitar su lectura. Facilitar el mantenimiento. Evitar concentrar todo el código en un único archivo. Reutilizar funciones. Facilitar futuras ampliaciones. Separar las responsabilidades de cada componente.

25. Importación de módulos
El proyecto utiliza importaciones para conectar los diferentes módulos.

Por ejemplo, main.py importa la configuración:

from app.config.settings import APP_NAME, APP_VERSION, ADMIN_USER

También importa el gestor de usuarios:

from app.usuarios.gestor import GestorUsuarios

Y gestor.py importa las funciones de validación:

from app.usuarios.validaciones import validar_nombre, validar_edad

Esto demuestra el uso de módulos y paquetes en Python.

26. Evidencias de aprendizaje
A continuación se agregarán las capturas de pantalla correspondientes al desarrollo del proyecto.

26.1 Creación del entorno virtual Evidencia: creación del entorno virtual utilizando venv. Creación del entorno virtual

26.2 Activación del entorno virtual Evidencia: entorno virtual activo mostrando (.venv) en la terminal. Activación del entorno virtual

26.3 Instalación de dependencias Evidencia: instalación de python-dotenv. Instalación de dependencias

26.4 Archivo requirements.txt Evidencia: archivo requirements.txt mostrando: python-dotenv==1.2.3 Archivo requirements.txt

26.5 Estructura modular Evidencia: estructura de carpetas y archivos del proyecto en Visual Studio Code. Insertar aquí la captura de pantalla.

26.6 Ejecución del sistema Evidencia: menú principal del sistema ejecutándose desde la terminal. Insertar aquí la captura de pantalla.

26.7 Registro de usuario Evidencia: registro exitoso de un usuario. Registro de usuario

26.8 Listado de usuarios Evidencia: listado de usuarios registrados. Insertar aquí la captura de pantalla.

26.9 Búsqueda de usuario Evidencia: búsqueda exitosa de un usuario. Insertar aquí la captura de pantalla.

26.10 Uso de variables de entorno Evidencia: configuración cargada desde .env. Resultado esperado:

Configuración del sistema Nombre de la aplicación: Sistema Usuarios Versión: 1.0 Usuario administrador: admin

Insertar aquí la captura de pantalla.

26.11 Validación de datos Evidencia: mensajes generados al ingresar datos incorrectos.

Ejemplos:

Error: El nombre no puede estar vacío. Error: La edad no puede ser negativa. Error: La edad ingresada no es válida. Error: La edad debe ser un número entero.

Validación de datos

Validación de datos

27. Reflexión final
El desarrollo de este proyecto permitió aplicar diferentes conceptos de Python avanzado en un escenario práctico.

Ventajas de modularizar

La modularización permite dividir una aplicación en componentes con responsabilidades específicas. En este proyecto se separaron la gestión de usuarios, las validaciones y la configuración.

Esto facilita la lectura del código, el mantenimiento y la posibilidad de agregar nuevas funcionalidades en el futuro sin modificar completamente el programa.

Importancia de aislar dependencias

El uso de entornos virtuales permite mantener las dependencias de cada proyecto aisladas.

Esto evita conflictos entre diferentes proyectos que pueden utilizar versiones distintas de una misma biblioteca.

Además, el archivo requirements.txt permite identificar y reproducir las dependencias necesarias para ejecutar el proyecto.

Uso seguro de variables de entorno

Las variables de entorno permiten separar información de configuración del código fuente.

En este proyecto se utilizó python-dotenv para cargar las variables desde el archivo .env.

El archivo .env se agregó al .gitignore para evitar que sea publicado accidentalmente en GitHub.

El archivo .env.example permite documentar las variables necesarias sin exponer la configuración privada.

28. Conclusión
El proyecto permitió integrar los conceptos estudiados sobre entornos virtuales, gestión de dependencias, variables de entorno y modularización.

La aplicación desarrollada cumple con las funcionalidades principales solicitadas en el reto y presenta una estructura organizada que facilita su mantenimiento y ampliación.

El uso de módulos, paquetes, excepciones, validaciones, venv, pip, requirements.txt y python-dotenv permitió construir una aplicación de consola organizada y aplicable a un escenario real de desarrollo en Python.

29. Video de reflexión final
En esta sección se agregará el enlace al video de YouTube correspondiente a la reflexión final sobre:

Ventajas de modularizar. Importancia de aislar dependencias. Uso seguro de variables de entorno.

Enlace del video:

Pegar aquí el enlace del video de YouTube.

30. Repositorio
El código fuente del proyecto se encuentra disponible en GitHub.

Repositorio:

Pegar aquí el enlace del repositorio de GitHub.

31. Autor
Aprendiz: GILLSON MARTINEZ

Programa de formación: SENA

Evidencia: GA1-220501093-04-AA1-EV06

Proyecto: Sistema Modular de Configuración y Gestión de Usuarios
