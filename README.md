# El_portafolio
Repositorio central de mis proyectos de desarrollo full stack de  web

## Formulario de contacto

El formulario envía los mensajes a Formspree. Crea un formulario en tu cuenta,
verifica allí la dirección de Gmail donde quieres recibir los mensajes y copia
el endpoint que te proporciona (por ejemplo, `https://formspree.io/f/abcxyz`).

Configura ese endpoint en un archivo `.env` en la raíz del proyecto:

```env
FORMSPREE_ENDPOINT=https://formspree.io/f/tu-id-de-formulario
```

La aplicación lee esta variable al iniciar. Reiníciala después de añadirla.
En producción, configura la misma variable en el proveedor de alojamiento.
No se necesita una contraseña de aplicación ni credenciales SMTP de Gmail.
