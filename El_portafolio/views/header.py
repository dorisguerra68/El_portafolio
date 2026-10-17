import reflex as rx

from El_portafolio.Styles.styles import (
    Color,
    Size,
    SUBTITLE_STYLE,
    TITLE_STYLE,
)
from El_portafolio.views.link import link


def header() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.vstack(
                rx.text(
                    "Doris Guerra",
                    **TITLE_STYLE,
                    color=Color.TEXT_DARK.value,
                    text_align=["center", "left"],
                ),
                rx.text(
                    "Desarrolladora Web Full Stack",
                    **SUBTITLE_STYLE,
                    color=Color.TEXT_MUTED.value,
                    text_align=["center", "left"],
                ),
                rx.text(
                    "Construyendo Soluciones Digitales 🚀.",
                    font_size=["1rem", "1.15rem", "1.3rem"],
                    color=Color.TEXT_MUTED.value,
                    text_align=["center", "left"],
                ),
                align_items=["center", "start"],
                spacing=rx.breakpoints(initial="2", sm="4", md="5"),
                width="100%",
                padding=["1rem 0.75rem", "0"],
                background_color=[
                    "rgba(250,250,255,0.82)",
                    "transparent",
                ],
                border_radius=["20px", "0"],
            ),
            rx.box(
                link(),
                margin_top=["0.75rem", Size.MEDIUM.value],
                width="100%",
            ),
            width="100%",
            align_items=["center", "start"],
            justify_content=["flex-end", "center"],
            padding=[
                "1.25rem 1rem 1.5rem",
                "4rem 2rem",
                f"{Size.BIG.value} {Size.MEDIUM.value}",
            ],
            background_image=[
                "linear-gradient(to bottom, rgba(250,250,255,0.02) 22%, rgba(250,250,255,0.35) 48%, rgba(250,250,255,0.98) 76%), url('/imagen/fondoDG2.webp')",
                "url('/imagen/fondoDG2.webp')",
            ],
            background_size="cover",
            background_position=["center center", "right center"],
            background_repeat="no-repeat",
            min_height=["82vh", "88vh", "100vh"],
            box_sizing="border-box",
        ),
        width="100%",
    )
