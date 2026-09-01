import reflex as rx

from El_portafolio.Styles.styles import (
    BUTTON_PRIMARY_STYLE,
    Color,
    NAVBAR_LINK_STYLE,
)


def navbar() -> rx.Component:
    return rx.center(
        rx.hstack(
            # Bloque Izquierdo: Logotipo
            rx.hstack(
                rx.avatar(
                    fallback="DG",
                    size="2",
                    background_color=Color.ACCENT_GOLD.value,
                    color=Color.TEXT_LIGHT.value,
                    variant="soft",
                ),
                rx.text(
                    "DevPortfolio",
                    font_size="1.5em",
                    weight="bold",
                    color=Color.TEXT_LIGHT.value,
                ),
                align="center",
                spacing="1",
            ),
            
            rx.spacer(),
                        # Bloque Derecho: Menú de Navegación
            rx.hstack(
                # Enlace: Inicio (con icono de casa)
                rx.link(
                    rx.hstack(
                        rx.icon("home", size=18),
                        rx.text("Inicio"),
                        align="center",
                        spacing="2",
                    ),
                    href="#inicio",
                    **NAVBAR_LINK_STYLE,
                ),
                
                # Enlace: Quién Soy (con icono de dashboard/layout)
                rx.link(
                    rx.hstack(
                        rx.icon("layout-dashboard", size=18),
                        rx.text("Quien Soy"),
                        align="center",
                        spacing="2",
                    ),
                    href="#quien-soy",
                    **NAVBAR_LINK_STYLE,
                ),
                
                # Enlace: Proyectos (con icono de carpeta/proyectos)
                rx.link(
                    rx.hstack(
                        rx.icon("square-library", size=18), 
                        rx.text("Proyectos"),
                        align="center",
                        spacing="2",
                    ),
                    href="#proyectos",
                    **NAVBAR_LINK_STYLE,
                ),
                
                # Botón: Contacto (con icono de mensaje/correo)
                rx.button(
                    rx.hstack(
                        rx.icon("mail", size=18), 
                        rx.text("Contacto"),
                        align="center",
                        spacing="2",
                    ),
                    **BUTTON_PRIMARY_STYLE,
                ),
                
                spacing="3", 
                align="center",
            ),

            align="center",
            width="100%",
            max_width="1500px",
            padding_x="2.5em",
            padding_y="0.9em",
        ),
        width="100%",
        background_color=Color.NAVBAR_BG.value,
        border_bottom=f"1px solid {Color.BORDER_GRAY.value}",
        box_shadow="0 4px 12px rgba(15, 23, 42, 0.08)",
        position="sticky",
        top="0",
        z_index="100",
    )
