import reflex as rx
from El_portafolio.components.navbar import navbar
from El_portafolio.components.footer import footer
from El_portafolio.views.header import header


def index():
    return rx.vstack(
        navbar(),
        header(),
        footer(),
        align="center",
    )


# Inicializamos la aplicación
app = rx.App(
    stylesheets=[
        "https://googleapis.com"
    ]
)
app.add_page(index)
