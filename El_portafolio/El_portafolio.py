import reflex as rx

from El_portafolio.components.footer import footer
from El_portafolio.components.navbar import navbar
from El_portafolio.views.about import about
from El_portafolio.views.contact import contact
from El_portafolio.views.header import header
from El_portafolio.views.project import project


def index():
    return rx.vstack(
        navbar(),
        header(),
        footer(),
        align="center",
    )


# Inicializamos la aplicación
app = rx.App()
app.add_page(index, title="Inicio")
app.add_page(project, route="/projects", title="Mis Proyectos")
app.add_page(about, title="Sobre mí")
app.add_page(contact, title="Contacto")
