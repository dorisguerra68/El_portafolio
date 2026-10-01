import reflex as rx

from El_portafolio.components.footer import footer
from El_portafolio.components.navbar import navbar
from El_portafolio.components.project_card import project_card
from El_portafolio.Styles.styles import Color, SUBTITLE_STYLE, TITLE_STYLE


PROJECTS = [
    {
        "title": "MovieStick",
        "subtitle": "Proyecto de entretenimiento",
        "description": "Una experiencia web relacionada con el cine.",
        "details": (
            "MovieStick es una propuesta web enfocada en presentar contenido "
            "de cine de manera visual y accesible. La página reúne una "
            "experiencia de exploración pensada para que las personas puedan "
            "conocer el proyecto y navegar por su catálogo."
        ),
        "image": "/imagen/img_MovieStick.png",
        "alt": "Identidad visual de MovieStick",
        "url": "https://moviestick.vercel.app/",
    },
    {
        "title": "Sabores que cuidan",
        "subtitle": "Comer sano sin perder el placer de comer",
        "description": "Proyectos y experiencias de desarrollo web.",
        "details": (
            "Sabores que cuidan presenta una propuesta centrada en la "
            "alimentación saludable, sin dejar de lado el disfrute de la "
            "comida. Su identidad busca comunicar bienestar y una relación "
            "amable con la cocina cotidiana."
        ),
        "image": "/imagen/weddg.webp",
        "alt": "Ilustración de un portafolio de desarrollo web",
        "url": "",
    },
    {
        "title": "MovieStick - Catálogo",
        "subtitle": "Interfaz de exploración",
        "description": "Vista para descubrir y explorar contenido de cine.",
        "details": (
            "Esta sección destaca la experiencia de explorar títulos de cine "
            "dentro de MovieStick. Su presentación visual ayuda a organizar "
            "el contenido y facilita recorrer las opciones disponibles."
        ),
        "image": "/imagen/img_MovieStick.png",
        "alt": "Identidad visual de MovieStick",
        "url": "",
    },
    {
        "title": "Portafolio profesional",
        "subtitle": "Diseño de experiencia web",
        "description": "Presentación de proyectos y habilidades digitales.",
        "details": (
            "Este portafolio reúne una selección de proyectos y habilidades "
            "de desarrollo web. Está pensado para presentar el trabajo de "
            "forma clara, con una navegación sencilla y una identidad visual "
            "coherente."
        ),
        "image": "/imagen/weddg.webp",
        "alt": "Ilustración de un portafolio de desarrollo web",
        "url": "",
    },
]


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
