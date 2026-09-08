import reflex as rx
from El_portafolio.components.footer import footer
from El_portafolio.components.navbar import navbar


@rx.page(route="/projects", title="Mis Proyectos")
def project() -> rx.Component:
    return rx.vstack(
        navbar(),  # Incorporamos el Navbar al inicio
        rx.grid(
            rx.foreach(
                rx.Var.range(3),
                lambda i: rx.card(
                    rx.inset(
                        rx.image(
                            src="https://web.reflex-assets.dev/other/reflex_banner.png",
                            alt="Reflex banner image",
                            width="100%",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    # Alternativa ultra-segura para concatenar texto con rx.Var
                    rx.text("Card ", (i + 1).to_string()), 
                ),
            ),
            gap="1rem",
            grid_template_columns=[
                "1fr",            # Móviles
                "repeat(2, 1fr)", # Tablets pequeñas
                "repeat(2, 1fr)", # Tablets
                "repeat(3, 1fr)", # Desktops
                "repeat(4, 1fr)", # Pantallas grandes
            ],
            width="100%",
        ),
        footer(),  # Incorporamos el Footer al final
        width="100%",
        spacing="4",
    )
