import datetime

import reflex as rx

from El_portafolio.Styles.styles import Color


def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(src="favicon.ico", box_size="2rem"),
            rx.text(
                "Doris Guerra",
                color=Color.FOOTER_TEXT.value,
                weight="bold",
                size="4",
            ),
            align="center",
            spacing="3",
            width="100%",
            justify="center",
        ),
        rx.text(
            f"© {datetime.datetime.now().year} - All rights reserved.",
            color=Color.FOOTER_TEXT.value,
            size="2",
        ),
        align="center",
        justify="center",
        width="100%",
        padding="1rem 1rem 1.5rem",
        margin_top="0",
        background_color=Color.FOOTER_BG.value,
        border_top=f"1px solid {Color.FOOTER_ALT.value}",
        box_shadow="inset 0 1px 0 rgba(255,255,255,0.7)",
    )
