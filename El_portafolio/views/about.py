import reflex as rx

from El_portafolio.components.footer import footer
from El_portafolio.components.navbar import navbar
from El_portafolio.Styles.styles import (
    Color,
    LAYOUT_SECTION_BASE,
    Size,
    SUBTITLE_STYLE,
    TITLE_STYLE,
)


@rx.page(route="/about", title="Sobre mí")
def about() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            rx.text(
                "Sobre mí",
                **TITLE_STYLE,
                color=Color.TEXT_DARK.value,
                text_align="center",
            ),
            rx.flex(
                rx.link(
                    rx.image(
                        src=(
                            "https://images.unsplash.com/"
                            "photo-1544005313-94ddf0286df2?"
                            "auto=format&fit=crop&w=900&q=80"
                        ),
                        alt="Retrato de Doris Guerra",
                        width="100%",
                        height="100%",
                        object_fit="cover",
                        border_radius="24px",
                        box_shadow="0 18px 40px rgba(30, 47, 93, 0.15)",
                    ),
                    href="https://www.linkedin.com",
                    is_external=True,
                    width="45%",
                    min_width="280px",
                    border_radius="24px",
                    overflow="hidden",
                ),
                rx.vstack(
                    rx.text(
                        "Desarrolladora Web Full Stack",
                        **SUBTITLE_STYLE,
                        color=Color.TEXT_MUTED.value,
                        font_size="2rem",
                        padding=Size.SMALL.value, 
                    ),
                    rx.text(
                        (
                            "Soy Doris Guerra, una desarrolladora "
                            "web Full Stack con pasión por crear "
                            "experiencias digitales claras, útiles "
                            "y visualmente atractivas."
                        ),
                        color=Color.TEXT_MUTED.value,
                        font_size="1.9rem",
                        line_height="1.8",
                        max_width="700px",
                        padding=Size.SMALL.value,                    ),
                    rx.text(
                        (
                            "Me especializo en el diseño y desarrollo "
                            "de soluciones modernas, con atención al "
                            "detalle, código limpio y una excelente "
                            "experiencia de usuario."
                        ),
                        color=Color.TEXT_MUTED.value,
                        font_size="1.9rem",
                        line_height="1.8",
                        max_width="700px",
                        padding=Size.SMALL.value, 
                    ),
                    align_items="start",
                    spacing="4",
                    flex="1",
                ),
                width="100%",
                max_width="1200px",
                align="center",
                justify="between",
                spacing="4",
                wrap="wrap",
            ),
            **LAYOUT_SECTION_BASE,
            padding=f"{Size.BIG.value} {Size.MEDIUM.value}",
            background=(
                "linear-gradient(135deg, rgba(250,250,255,1) 0%, "
                "rgba(240,243,252,1) 100%)"
            ),
            min_height="calc(100vh - 160px)",
            spacing="6",
            align="center",
        ),
        footer(),
        width="100%",
    )
