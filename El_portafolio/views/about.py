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
from El_portafolio.Styles.stylesNocturno import themed_page


def about() -> rx.Component:
    return themed_page(
        rx.vstack(
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
                            src="/imagen/imgDG5.jpeg",
                            alt="Retrato de Doris Guerra",
                            width="100%",
                            height="auto",
                            object_fit="contain",
                            border_radius="24px",
                            box_shadow="0 18px 40px rgba(30, 47, 93, 0.15)",
                        ),
                        href="https://www.linkedin.com",
                        is_external=True,
                        width=["100%", "42%"],
                        min_width=["0", "280px"],
                        max_width="420px",
                        border_radius="24px",
                        overflow="hidden",
                        flex_shrink="0",
                    ),
                    rx.vstack(
                        rx.text(
                            "Transformo ideas en soluciones web funcionales, "
                            "combinando técnica y empatía.",
                            **{**SUBTITLE_STYLE, "weight": "bold"},
                            color=Color.TEXT_MUTED.value,
                            font_size=["1.25rem", "1.45rem", "1.65rem"],
                            padding=Size.SMALL.value,
                        ),
                        rx.text(
                            (
                                "¡Hola! Vivo en Aranjuez (Madrid) y soy "
                                "Desarrolladora Web Full Stack. Mi camino "
                                "hasta el mundo del código no ha sido "
                                "lineal, y ese es precisamente mi mayor "
                                "valor diferencial: entiendo perfectamente "
                                "las necesidades reales de las personas."
                            ),
                            color=Color.TEXT_MUTED.value,
                            font_size=["1rem", "1.05rem", "1.1rem"],
                            line_height="1.8",
                            max_width="700px",
                            padding=Size.SMALL.value,
                        ),
                        rx.text(
                            "Mi trayectoria incluye experiencia "
                            "internacional entre Venezuela, Italia y "
                            "España. Antes de dedicarme al desarrollo web, "
                            "trabajé en administración y atención al "
                            "paciente, gestioné documentación de forma "
                            "autónoma, brindé soporte técnico informático "
                            "a particulares (tras formarme en sistemas "
                            "microinformáticos) y dediqué años al cuidado "
                            "de personas mayores y niños, etapa que me "
                            "enseñó el valor de la paciencia, la escucha "
                            "activa y el compromiso.",
                            color=Color.TEXT_MUTED.value,
                            font_size=["1rem", "1.05rem", "1.1rem"],
                            line_height="1.8",
                            max_width="700px",
                            padding=Size.SMALL.value,
                        ),
                        rx.text(
                            "Tras formarme intensivamente en el bootcamp "
                            "de ",
                            rx.text.span("Factoría F5", weight="bold"),
                            ", hoy ayudo a negocios, profesionales y "
                            "particulares a construir su presencia digital. "
                            "Desarrollo páginas y aplicaciones web a medida, "
                            "cuidando tanto el código como la experiencia "
                            "del usuario. Si buscas a alguien resolutiva, "
                            "organizada y con verdadera vocación de servicio "
                            "para tu próximo proyecto o equipo, ¡hablemos!",
                            color=Color.TEXT_MUTED.value,
                            font_size=["1rem", "1.05rem", "1.1rem"],
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
                    spacing=rx.breakpoints(initial="4", sm="5"),
                    wrap="wrap",
                    padding_x=["0", "0.5rem"],
                ),
                **LAYOUT_SECTION_BASE,
                padding=[
                    "2.5rem 1rem",
                    "3.5rem 2rem",
                    f"{Size.BIG.value} {Size.MEDIUM.value}",
                ],
                background="var(--portfolio-page-background)",
                min_height="calc(100vh - 160px)",
                spacing="6",
                align="center",
            ),
            footer(),
            width="100%",
        )
    )
