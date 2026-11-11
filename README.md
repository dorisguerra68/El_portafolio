# Portafolio de Doris Guerra

Portafolio personal desarrollado con [Reflex](https://reflex.dev/) y Python.
Presenta información sobre mí, una selección de proyectos y una página de
contacto con formulario. La interfaz se adapta a móviles, tabletas y escritorio
e incluye modo claro y oscuro.

## Contenido

- [Portafolio de Doris Guerra](#portafolio-de-doris-guerra)
  - [Contenido](#contenido)
  - [Requisitos](#requisitos)
  - [Descargar el proyecto](#descargar-el-proyecto)
  - [Instalar y ejecutar](#instalar-y-ejecutar)
  - [Uso de la aplicación](#uso-de-la-aplicación)
  - [Diseño responsive](#diseño-responsive)
  - [Configurar el formulario y el correo](#configurar-el-formulario-y-el-correo)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Actualizar el proyecto](#actualizar-el-proyecto)
  - [Tecnologías](#tecnologías)

## Requisitos

- Git.
- Python 3.10 o posterior.
- Una conexión a Internet para instalar las dependencias.

## Descargar el proyecto

Clona el repositorio de GitHub y entra en la carpeta creada:

```powershell
git clone https://github.com/dorisguerra68/El_portafolio.git
cd El_portafolio
```

En Windows también puedes descargar el repositorio desde GitHub como archivo
ZIP y extraerlo. Si eliges esa opción, abre una terminal dentro de la carpeta
extraída antes de continuar.

## Instalar y ejecutar

Los siguientes comandos están pensados para Windows PowerShell. Se recomienda
crear un entorno virtual para mantener las dependencias del proyecto separadas
de las del sistema:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
reflex run
```

`requirements.txt` instala Reflex y las dependencias del proyecto en las
versiones especificadas. Cuando Reflex termine de iniciar, abre
<http://localhost:3000> en el navegador. Mantén abierta la terminal mientras
uses la aplicación; para detenerla, pulsa `Ctrl+C`.

Si PowerShell impide activar el entorno virtual, puedes habilitar la ejecución
de scripts solo para la terminal actual y volver a activarlo:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

En macOS o Linux, la creación y activación del entorno virtual se realiza así;
los pasos restantes (`pip install` y `reflex run`) son los mismos:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Este repositorio ya contiene la configuración de Reflex (`rxconfig.py`) y la
aplicación. No es necesario ejecutar `reflex init` al descargarlo.

## Uso de la aplicación

La barra de navegación permite visitar estas secciones:

| Sección | Ruta | Contenido |
| --- | --- | --- |
| Inicio | `/` | Presentación principal. |
| Sobre mí | `/about` | Trayectoria y perfil profesional. |
| Proyectos | `/projects` | Selección de trabajos y enlaces a los proyectos. |
| Contacto | `/contact` | Datos de contacto y formulario de mensajes. |

En móviles y tabletas, abre el menú de navegación con el botón de menú. El
botón con el icono de luna o sol cambia entre modo oscuro y claro.

En la página Contacto puedes:

1. Abrir un mensaje nuevo a `loretodoris68@gmail.com` con el enlace de correo.
   Esto abre la aplicación de correo configurada en tu dispositivo.
2. Completar el formulario con nombre, correo electrónico y mensaje. Al enviarlo,
   la aplicación remite los datos a Formspree; cuando el envío se completa,
   aparece una confirmación en la página.

## Diseño responsive

Las páginas utilizan estilos adaptables de Reflex y puntos de quiebre para
ajustar tamaños, espaciado y distribución según el ancho disponible. En
pantallas pequeñas, los bloques y tarjetas se organizan en una columna; en
pantallas mayores aprovechan varias columnas cuando corresponde. La navegación
usa un menú desplegable en móvil y tableta, y enlaces visibles en escritorio.
Las imágenes conservan su proporción para evitar recortes no deseados.

Para ajustar el diseño, consulta principalmente:

- `El_portafolio/Styles/styles.py`: estilos y tamaños compartidos.
- `El_portafolio/Styles/stylesNocturno.py`: colores y modo claro/oscuro.
- `El_portafolio/components/navbar.py`: navegación y menú móvil.
- `El_portafolio/views/`: composición de las páginas.

## Configurar el formulario y el correo

El formulario utiliza [Formspree](https://formspree.io/) para entregar los
mensajes. El enlace `mailto:` de la página de contacto y el destinatario del
formulario son mecanismos distintos: el primero abre el correo del visitante;
el segundo envía el mensaje a la dirección configurada en la cuenta de
Formspree.

Para activar la recepción de mensajes:

1. Crea una cuenta en Formspree y configura un formulario nuevo.
2. En los ajustes del formulario, establece la dirección donde quieres recibir
   los mensajes. Para este portafolio, utiliza `mi correo` si
   deseas recibirlos en el mismo correo de contacto.
3. Verifica esa dirección siguiendo las instrucciones que Formspree envía a
   tu correo.
4. Copia el endpoint del formulario que te proporciona Formspree, con un
   formato similar a `https://formspree.io/h/abcxyz`.
5. Crea un archivo llamado `.env` en la carpeta raíz del proyecto (junto a
   `rxconfig.py`) y añade:

   ```env
   FORMSPREE_ENDPOINT=https://formspree.io/f/tu-id-de-formulario
   ```

6. Guarda el archivo y reinicia la aplicación con `reflex run`.

El código lee `FORMSPREE_ENDPOINT` desde `.env` al iniciar y realiza el envío
desde el servidor. Sin esta variable, el formulario muestra un aviso y no envía
mensajes; el enlace de correo directo continúa disponible. Si Formspree rechaza
el envío o hay un problema de conexión, la página informa que no se pudo enviar
para que la persona pueda intentarlo de nuevo.

El archivo `.env` está excluido de Git mediante `.gitignore`: no lo publiques ni
añadas credenciales privadas al repositorio. En un alojamiento de producción,
configura `FORMSPREE_ENDPOINT` como variable de entorno en la plataforma y
verifica la dirección destinataria en Formspree. No se requiere contraseña de
Gmail ni configuración SMTP.

## Estructura del proyecto

```text
El_portafolio/
├── El_portafolio/
│   ├── components/       # Navegación, formulario, tarjetas y pie de página
│   ├── Styles/           # Estilos compartidos y temas
│   ├── views/            # Páginas de inicio, proyectos, perfil y contacto
│   └── El_portafolio.py  # Registro de rutas y aplicación Reflex
├── assets/               # Imágenes y otros recursos visuales
├── requirements.txt      # Dependencias de Python
└── rxconfig.py           # Configuración de Reflex
```

## Actualizar el proyecto

Para obtener los cambios más recientes de GitHub, abre una terminal en la
carpeta del repositorio y ejecuta:

```powershell
git pull
```

Si se actualizaron las dependencias, activa el entorno virtual y vuelve a
instalarlas:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Después, inicia o reinicia la aplicación:

```powershell
reflex run
```

## Tecnologías

- Python
- [Reflex](https://reflex.dev/)
- Formspree para el formulario de contacto
