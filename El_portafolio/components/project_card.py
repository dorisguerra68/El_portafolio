import reflex as rx

from El_portafolio.Styles.styles import Color, SUBTITLE_STYLE


class ProjectCardState(rx.State):
    open_project: str = ""

    @rx.event
    def toggle_details(self, project_title: str):
        if self.open_project == project_title:
            self.open_project = ""
        else:
            self.open_project = project_title

    @rx.event
    def close_details(self):
        self.open_project = ""


def project_card(
    title: str,
    subtitle: str,
    description: str,
    details: str,
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
            on_click=ProjectCardState.close_details,
            cursor="pointer",
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
            rx.button(
                rx.cond(
                    ProjectCardState.open_project == title,
                    "Cerrar información -",
                    "Más información +",
                ),
                on_click=ProjectCardState.toggle_details(title),
                variant="outline",
                color=Color.NAVBAR_BG.value,
                border_color=Color.NAVBAR_BG.value,
                cursor="pointer",
                _hover={
                    "background_color": Color.FOOTER_BG.value,
                },
            ),
            rx.cond(
                ProjectCardState.open_project == title,
                rx.box(
                    rx.text(
                        details,
                        color=Color.TEXT_MUTED.value,
                        line_height="1.7",
                    ),
                    width="100%",
                    padding="1rem",
                    background_color=Color.FOOTER_BG.value,
                    border_left=f"3px solid {Color.ACCENT_GOLD.value}",
                    border_radius="8px",
                ),
                rx.box(),
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
