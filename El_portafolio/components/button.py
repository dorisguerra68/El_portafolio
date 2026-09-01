import reflex as rx

from El_portafolio.Styles.styles import BUTTON_PRIMARY_STYLE


def button(text: str, url: str) -> rx.Component:
    return rx.button(
        text,
        # Estilo global compartido para todos los botones principales.
        **BUTTON_PRIMARY_STYLE,
        # Redirección externa para abrir el enlace en nueva pestaña.
        on_click=rx.redirect(url, is_external=True),
    )
