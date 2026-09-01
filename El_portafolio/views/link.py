import reflex as rx
from El_portafolio.components.button import button


def link() -> rx.Component:
    return rx.hstack(
        button(
            "Visit My Website",
            "https://www.youtube.com/@LosTemerariosy00",
        ),
        button("LinkedIn", "https://www.linkedin.com/in/doris-guerra"),
        button(
            "Check Out My GitHub",
            "https://github.com/dorisguerra68",
        ),
        width="100%",
        spacing="3",
        flex_wrap="wrap",
    )
