import reflex as rx

from El_portafolio.Styles.styles import (
    BUTTON_PRIMARY_STYLE,
    Color,
    NAVBAR_LINK_STYLE,
)


def _nav_link(label: str, icon: str, href: str, primary: bool = False) -> rx.Component:
    style = BUTTON_PRIMARY_STYLE if primary else NAVBAR_LINK_STYLE
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(label),
            align="center",
            spacing="2",
        ),
        href=href,
        **style,
    )


def _nav_links(mobile: bool = False) -> rx.Component:
    return rx.flex(
        _nav_link("Inicio", "home", "/"),
        _nav_link("Sobre mí", "layout-dashboard", "/about"),
        _nav_link("Proyectos", "square-library", "/projects"),
        _nav_link("Contacto", "mail", "/contact", primary=True),
        direction="column" if mobile else "row",
        spacing="2" if mobile else rx.breakpoints(initial="1", sm="2", md="3"),
        align="stretch" if mobile else "center",
        justify="center",
        flex_wrap="wrap",
        width="100%" if mobile else ["100%", "100%", "auto"],
    )


def navbar() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
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
                        font_size=["1.15em", "1.3em", "1.5em"],
                        weight="bold",
                        color=Color.TEXT_LIGHT.value,
                        letter_spacing="0.04em",
                    ),
                    align="center",
                    spacing="2",
                    flex_shrink="0",
                ),
                rx.mobile_and_tablet(
                    rx.el.details(
                        rx.el.summary(
                            rx.icon("menu", size=22),
                            aria_label="Abrir menú de navegación",
                            title="Abrir menú",
                            list_style="none",
                            cursor="pointer",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            color=Color.TEXT_LIGHT.value,
                            background_color="rgba(255,255,255,0.12)",
                            border_radius="12px",
                            padding="0.55rem",
                            _hover={
                                "background_color": "rgba(255,255,255,0.22)"
                            },
                        ),
                        rx.box(
                            _nav_links(mobile=True),
                            position="absolute",
                            top="calc(100% + 0.75rem)",
                            right="0",
                            width="min(88vw, 20rem)",
                            padding="0.75rem",
                            background_color=Color.NAVBAR_BG.value,
                            border="1px solid rgba(255,255,255,0.12)",
                            border_radius="14px",
                            box_shadow="0 12px 28px rgba(17, 24, 39, 0.28)",
                        ),
                        position="relative",
                    ),
                ),
                rx.desktop_only(_nav_links()),
                width="100%",
                align="center",
                justify="between",
            ),
            width="100%",
            align_items="stretch",
            spacing="3",
            max_width="1200px",
            padding_x=["0.75rem", "1.25rem", "2rem"],
            padding_y=["0.75rem", "0.85rem", "0.9rem"],
            border_radius="20px",
            background_color=Color.NAVBAR_BG.value,
            box_shadow="0 10px 30px rgba(17, 24, 39, 0.18)",
            border="1px solid rgba(255,255,255,0.08)",
        ),
        width="100%",
        padding_x=["0.5rem", "0.75rem", "1rem"],
        padding_y=["0.5rem", "0.75rem", "1rem"],
        background_color="rgba(30, 47, 93, 0.96)",
        border_bottom=f"1px solid {Color.BORDER_GRAY.value}",
        backdrop_filter="blur(12px)",
        position="sticky",
        top="0",
        z_index="100",
    )
