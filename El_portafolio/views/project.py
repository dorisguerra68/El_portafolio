import reflex as rx

from El_portafolio.Styles.styles import Color, SUBTITLE_STYLE, TITLE_STYLE
from El_portafolio.components.footer import footer
from El_portafolio.components.navbar import navbar


PROJECTS = [
    {
        "title": "MovieStick",
        "subtitle": "Proyecto de entretenimiento",
        "description": "Una experiencia web relacionada con el cine.",
        "image": "/imagen/img_MovieStick.png",
        "alt": "Identidad visual de MovieStick",
        "url": "https://moviestick.vercel.app/",
    },
    {
        "title": "Mi portafolio",
        "subtitle": "Desarrollo web Full Stack",
        "description": "Proyectos y experiencias de desarrollo web.",
        "image": "/imagen/weddg.webp",
        "alt": "Ilustración de un portafolio de desarrollo web",
        "url": "",
    },
    {
        "title": "MovieStick - Catálogo",
        "subtitle": "Interfaz de exploración",
        "description": "Vista para descubrir y explorar contenido de cine.",
        "image": "/imagen/img_MovieStick.png",
        "alt": "Identidad visual de MovieStick",
        "url": "",
    },
    {
        "title": "Portafolio profesional",
        "subtitle": "Diseño de experiencia web",
        "description": "Presentación de proyectos y habilidades digitales.",
        "image": "/imagen/weddg.webp",
        "alt": "Ilustración de un portafolio de desarrollo web",
        "url": "",
    },
]


def project_card(
    title: str,
    subtitle: str,
    description: str,
    image: str,
    alt: str,
    url: str,
) -> rx.Component:
    if url:
        project_link = rx.link(
            rx.hstack(
                rx.text("Visitar proyecto"),
                rx.icon("external-link", size=16),
                align="center",
                spacing="2",
            ),
            href=url,
            is_external=True,
            color=Color.TEXT_LIGHT.value,
            background_color=Color.NAVBAR_BG.value,
            padding="0.7em 1em",
            border_radius="10px",
            font_weight="600",
            transition="background-color 180ms ease, transform 180ms ease",
            _hover={
                "background_color": Color.ACCENT_GOLD.value,
                "transform": "translateY(-2px)",
            },
        )
    else:
        project_link = rx.button(
            "Enlace pendiente",
            disabled=True,
            color=Color.TEXT_LIGHT.value,
            background_color=Color.NAVBAR_BG.value,
            opacity="0.6",
            cursor="not-allowed",
            padding="0.7em 1em",
            border_radius="10px",
        )

    return rx.vstack(
        rx.image(
            src=image,
            alt=alt,
            width="100%",
            height="240px",
            object_fit="cover",
        ),
        rx.vstack(
            rx.text(
                title,
                **SUBTITLE_STYLE,
                color=Color.TEXT_DARK.value,
                font_size="1.5rem",
            ),
            rx.text(
                subtitle,
                color=Color.TEXT_MUTED.value,
                font_weight="600",
            ),
            rx.text(
                description,
                color=Color.TEXT_MUTED.value,
                line_height="1.6",
            ),
            project_link,
            width="100%",
            align_items="start",
            padding="1.25rem",
            spacing="3",
        ),
        width="100%",
        height="100%",
        spacing="0",
        background_color="white",
        border=f"1px solid {Color.NAVBAR_BG.value}",
        border_left=f"5px solid {Color.NAVBAR_BG.value}",
        border_radius="14px",
        overflow="hidden",
        box_shadow="0 8px 24px rgba(30, 47, 93, 0.14)",
        transition=(
            "transform 180ms ease, box-shadow 180ms ease, "
            "border-color 180ms ease"
        ),
        _hover={
            "transform": "translateY(-5px) scale(1.015)",
            "box_shadow": "0 16px 34px rgba(30, 47, 93, 0.22)",
            "border_color": Color.ACCENT_GOLD.value,
        },
    )


@rx.page(route="/projects", title="Mis Proyectos")
def project() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            rx.text(
                "Mis proyectos",
                **TITLE_STYLE,
                color=Color.TEXT_DARK.value,
                text_align="center",
            ),
            rx.text(
                "Una selección de mis trabajos de desarrollo web",
                **SUBTITLE_STYLE,
                color=Color.TEXT_MUTED.value,
                text_align="center",
                font_size="1.4rem",
            ),
            rx.grid(
                *[project_card(**item) for item in PROJECTS],
                gap="1.5rem",
                grid_template_columns=[
                    "1fr",
                    "repeat(2, minmax(0, 1fr))",
                ],
                width="100%",
                max_width="1200px",
            ),
            width="100%",
            align_items="center",
            padding=["2rem 1rem", "3rem 2rem"],
            spacing="5",
            background=(
                "linear-gradient(135deg, rgba(250,250,255,1) 0%, "
                "rgba(240,243,252,1) 100%)"
            ),
        ),
        footer(),
        width="100%",
        spacing="0",
    )
