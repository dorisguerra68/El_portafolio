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
        "alt": "Portada de MovieStick con logotipo y botón Entrar",
        "url": "https://moviestick.vercel.app/",
    },
    {
        "title": "Sabores que cuidan",
        "subtitle": "Comer sano sin perder el placer de comer",
        "description": "Proyectos y experiencias de desarrollo web.",
        "details": (
            "Aplicación web Full Stack que ayuda a mejorar los hábitos "
            "alimenticios mediante el registro diario de comidas y el "
            "seguimiento del progreso. Promueve una alimentación saludable "
            "sin dejar de lado el placer de comer."
        ),
            "details_heading": "EN CONSTRUCCIÓN",
            "details_image": "/imagen/enconstruccion.jpg",
        "image": "/imagen/saboresquecuidan.png",
        "alt": (
            "Logotipo Sabores que cuidan: hojas verdes sobre una mano "
            "y el nombre del proyecto"
        ),
        "url": "https://frontend-sabores-que-cuidan-alpha.vercel.app/",
    },
    {
        "title": "Content Enrichment",
        "subtitle": "Herramienta_consulta_wikipedia",
        "description": "Herramienta que enriquece de texto.",
        "details": (
            "Esta herramienta permite al usuario introducir un tema,  "
            "consultar Wikipedia mediante scraping, "
            "extraer el contenido principal, enriquecerlo con IA,"
            "traducirlo a cualquier idioma y exportarlo en formato text y PDF."
        ),
        "image": "/imagen/Scraping_Wikipedia.png",
        "alt": (
            "Captura de la herramienta de Wikipedia que consulta, "
            "enriquece y traduce artículos"
        ),
        "url": (
            "https://github.com/dorisguerra68/"
            "herramienta_consulta_wikipedia"
        ),
    },
    {
        "title": "LinkBio",
        "subtitle": "Diseño de experiencia web",
        "description": "Presentación de proyectos y habilidades digitales.",
        "details": (
            "Este portafolio reúne una selección de proyectos y habilidades "
            "de desarrollo web. Está pensado para presentar el trabajo de "
            "forma clara, con una navegación sencilla y una identidad visual "
            "coherente."
        ),
        "details_heading": "EN CONSTRUCCIÓN",
        "details_image": "/imagen/enconstruccion.jpg",
        "image": "/imagen/linkbio_doris.png",
        "alt": (
            "Perfil LinkBio de Doris Guerra con foto y accesos al portafolio, "
            "blogs, Instagram y contacto"
        ),
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
