import reflex as rx

from El_portafolio.components.formulario import formulario_contacto
from El_portafolio.components.footer import footer
from El_portafolio.components.navbar import navbar
from El_portafolio.Styles.styles import (
    Color,
    LAYOUT_SECTION_BASE,
    Size,
    SUBTITLE_STYLE,
    TITLE_STYLE,
)


def contact() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            rx.text(
                "Contacto",
                **TITLE_STYLE,
                color=Color.TEXT_DARK.value,
                text_align="center",
            ),
            rx.text(
                "Estoy disponible para proyectos, colaboraciones y oportunidades laborales.",
                **SUBTITLE_STYLE,
                color=Color.TEXT_MUTED.value,
                text_align="center",
            ),
            rx.flex(
                rx.vstack(
                    rx.text(
                        "Hablemos",
                        font_size=["1.5rem", "1.75rem", "2rem"],
                        font_weight="700",
                        color=Color.TEXT_DARK.value,
                    ),
                    rx.text(
                        "Si tienes una idea, un proyecto o quieres trabajar juntos, puedes escribirme directamente.",
                        color=Color.TEXT_MUTED.value,
                        line_height="1.7",
                        max_width=["100%", "420px"],
                    ),
                    rx.vstack(
                        rx.link(
                            "✉️ contacto@dorisguerra.dev",
                            href="mailto:contacto@dorisguerra.dev",
                            color=Color.TEXT_DARK.value,
                            font_weight="600",
                            word_break="break-word",
                        ),
                        rx.link(
                            "💼 linkedin.com/in/dorisguerra",
                            href="https://www.linkedin.com",
                            is_external=True,
                            color=Color.TEXT_DARK.value,
                            font_weight="600",
                            word_break="break-word",
                        ),
                        rx.link(
                            "🐙 github.com/dorisguerra68",
                            href="https://github.com/dorisguerra68",
                            is_external=True,
                            color=Color.TEXT_DARK.value,
                            font_weight="600",
                            word_break="break-word",
                        ),
                        spacing="3",
                        align_items="start",
                        width="100%",
                    ),
                    spacing="4",
                    align_items="start",
                    flex="1",
                    width="100%",
                    min_width="0",
                    flex_basis=["100%", "100%", "38%"],
                ),
                formulario_contacto(),
                align="center",
                justify="between",
                spacing=rx.breakpoints(initial="4", sm="5", md="6"),
                wrap="wrap",
                width="100%",
                max_width="1100px",
            ),
            rx.text(
                "Gracias por visitar mi portafolio.",
                **SUBTITLE_STYLE,
                color=Color.TEXT_MUTED.value,
                text_align="center",
            ),
            **LAYOUT_SECTION_BASE,
            padding=["2.5rem 1rem", "3.5rem 2rem", f"{Size.BIG.value} {Size.MEDIUM.value}"],
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
