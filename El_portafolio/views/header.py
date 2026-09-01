import reflex as rx

from El_portafolio.Styles.styles import (
    Color,
    LAYOUT_SECTION_BASE,
    Size,
    SUBTITLE_STYLE,
    TITLE_STYLE,
)
from El_portafolio.views.link import link


def header() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            # Bloque de textos
            rx.vstack(
                # Aplicamos la fuente Emilys Candy usando **TITLE_STYLE
                rx.text(
                    "Doris Guerra",
                    **TITLE_STYLE,
                    color=Color.TEXT_DARK.value,
                ),
                # Aplicamos la fuente Agbalumo usando **SUBTITLE_STYLE
                rx.text(
                    "Desarrolladora Web Full Stack",
                    **SUBTITLE_STYLE,
                    color=Color.TEXT_MUTED.value,
                ),
                # Texto común para eslogan (se mantiene limpio)
                rx.text(
                    "Construyendo Soluciones Digitales 🚀.",
                    size="5",
                    color=Color.TEXT_MUTED.value,
                ),
                align_items="start",
                spacing="5",
                width="100%",
            ),
            rx.hstack(
                link(),
                justify="start",
                spacing="4",
                margin_top=Size.MEDIUM.value,
                width="100%",
                flex_wrap="wrap",
            ),
            **LAYOUT_SECTION_BASE,
            padding=f"{Size.BIG.value} {Size.MEDIUM.value}",
            background_image="url('imagen/weddg.webp')",
            background_size="cover",
            background_position="right center",
            background_repeat="no-repeat",
            min_height="150vh",
        ),
        width="100%",
    )
