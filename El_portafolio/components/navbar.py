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
                    letter_spacing="0.04em",
                ),
                align="center",
                spacing="2",
            ),

            rx.spacer(),

            # Bloque Derecho: Menú de Navegación
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.icon("home", size=18),
                        rx.text("Inicio"),
                        align="center",
                        spacing="2",
                    ),
                    href="/",
                    **NAVBAR_LINK_STYLE,
                ),

                rx.link(
                    rx.hstack(
                        rx.icon("layout-dashboard", size=18),
                        rx.text("Sobre mí"),
                        align="center",
                        spacing="2",
                    ),
                    href="/about",
                    **NAVBAR_LINK_STYLE,
                ),

                rx.link(
                    rx.hstack(
                        rx.icon("square-library", size=18),
                        rx.text("Proyectos"),
                        align="center",
                        spacing="2",
                    ),
                    href="/projects",
                    **NAVBAR_LINK_STYLE,
                ),

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
            max_width="1200px",
            padding_x="2em",
            padding_y="0.9em",
            border_radius="20px",
            background_color=Color.NAVBAR_BG.value,
            box_shadow="0 10px 30px rgba(17, 24, 39, 0.18)",
            border="1px solid rgba(255,255,255,0.08)",
        ),
        width="100%",
        padding_x="1rem",
        padding_y="1rem",
        background_color="rgba(30, 47, 93, 0.96)",
        border_bottom=f"1px solid {Color.BORDER_GRAY.value}",
        backdrop_filter="blur(12px)",
        position="sticky",
        top="0",
        z_index="100",
    )
