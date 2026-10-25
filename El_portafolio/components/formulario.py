import logging
import os
from pathlib import Path

import httpx
import reflex as rx


logger = logging.getLogger(__name__)


def cargar_variables_entorno() -> None:
    rutas = [
        Path.cwd() / ".env",
        Path(__file__).resolve().parents[2] / ".env",
        Path(__file__).resolve().parent.parent / ".env",
    ]

    for ruta in rutas:
        if not ruta.exists():
            continue
        for linea in ruta.read_text(encoding="utf-8").splitlines():
            texto = linea.strip()
            if not texto or texto.startswith("#") or "=" not in texto:
                continue
            clave, valor = texto.split("=", 1)
            os.environ.setdefault(
                clave.strip(), valor.strip().strip('"').strip("'")
            )


def obtener_endpoint_formspree() -> str:
    cargar_variables_entorno()
    return os.getenv("FORMSPREE_ENDPOINT", "").strip()


class ContactState(rx.State):
    nombre: str = ""
    email: str = ""
    mensaje: str = ""
    enviado: bool = False
    error: str = ""

    @rx.event
    async def handle_submit(self, form_data: dict):
        self.nombre = str(form_data.get("nombre", "")).strip()
        self.email = str(form_data.get("email", "")).strip()
        self.mensaje = str(form_data.get("mensaje", "")).strip()
        self.enviado = False
        self.error = ""

        if not self.nombre or not self.email or not self.mensaje:
            self.error = "Completa todos los campos antes de enviar."
            return

        endpoint = obtener_endpoint_formspree()
        if not endpoint:
            self.error = (
                "El formulario aún no está configurado. "
                "Puedes escribirme directamente por correo."
            )
            return

        payload = {
            "nombre": self.nombre,
            "email": self.email,
            "_replyto": self.email,
            "_subject": f"Nuevo mensaje de contacto: {self.nombre}",
            "mensaje": self.mensaje,
        }

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.post(
                    endpoint,
                    data=payload,
                    headers={"Accept": "application/json"},
                )
                response.raise_for_status()
        except httpx.HTTPError:
            logger.exception("No se pudo enviar el mensaje a Formspree.")
            self.error = "No se pudo enviar el mensaje. Inténtalo de nuevo más tarde."
            return

        self.nombre = ""
        self.email = ""
        self.mensaje = ""
        self.enviado = True

    @rx.event
    def reset_form(self):
        self.enviado = False
        self.error = ""
        self.nombre = ""
        self.email = ""
        self.mensaje = ""


def formulario_contacto() -> rx.Component:
    aviso_configuracion = (
        rx.box(
            rx.text(
                "Añade FORMSPREE_ENDPOINT al archivo .env para activar el envío.",
                color="#92400e",
                font_weight="600",
            ),
            background_color="#fffbeb",
            border="1px solid rgba(217, 119, 6, 0.25)",
            border_radius="16px",
            padding="0.85rem 1rem",
            width="100%",
        )
        if not obtener_endpoint_formspree()
        else rx.box(width="100%")
    )

    campos_formulario = rx.vstack(
        rx.cond(
            ContactState.error != "",
            rx.box(
                rx.text(
                    ContactState.error,
                    color="#b91c1c",
                    font_weight="600",
                ),
                background_color="#fef2f2",
                border="1px solid rgba(220, 38, 38, 0.22)",
                border_radius="16px",
                padding="0.85rem 1rem",
                width="100%",
            ),
            rx.box(width="100%"),
        ),
        rx.text("Nombre completo", size="2", weight="bold", color="#1e2f5d"),
        rx.input(
            placeholder="Tu nombre",
            name="nombre",
            is_required=True,
            width="100%",
            height="3.5rem",
            box_sizing="border-box",
            border_radius="16px",
            border="1px solid rgba(30, 47, 93, 0.18)",
            padding_x="1rem",
            color="#1e2f5d",
            background_color="#ffffff",
            font_size="1rem",
            line_height="1.5",
            box_shadow="0 2px 6px rgba(30, 47, 93, 0.04)",
            _placeholder={"color": "#6b7280", "opacity": "1"},
        ),
        rx.text("Correo electrónico", size="2", weight="bold", color="#1e2f5d"),
        rx.input(
            placeholder="correo@ejemplo.com",
            type="email",
            name="email",
            is_required=True,
            width="100%",
            height="3.5rem",
            box_sizing="border-box",
            border_radius="16px",
            border="1px solid rgba(30, 47, 93, 0.18)",
            padding_x="1rem",
            color="#1e2f5d",
            background_color="#ffffff",
            font_size="1rem",
            line_height="1.5",
            box_shadow="0 2px 6px rgba(30, 47, 93, 0.04)",
            _placeholder={"color": "#6b7280", "opacity": "1"},
        ),
        rx.text("Mensaje", size="2", weight="bold", color="#1e2f5d"),
        rx.text_area(
            placeholder="Cuéntame sobre tu proyecto, idea o colaboración...",
            name="mensaje",
            is_required=True,
            width="100%",
            height="150px",
            border_radius="16px",
            border="1px solid rgba(30, 47, 93, 0.18)",
            padding="0.85rem 1rem",
            box_shadow="0 2px 6px rgba(30, 47, 93, 0.04)",
        ),
        rx.button(
            "Enviar mensaje",
            type="submit",
            width="100%",
            margin_top="0.5rem",
            background_color="#1e2f5d",
            color="#f2f2f6",
            border_radius="16px",
            padding_y="0.9rem",
            font_weight="600",
            box_shadow="0 10px 25px rgba(30, 47, 93, 0.2)",
            _hover={
                "background_color": "#234a73",
                "transform": "translateY(-1px)",
            },
        ),
        spacing="3",
        align="stretch",
        width="100%",
    )

    return rx.box(
        rx.form(
            rx.vstack(
                aviso_configuracion,
                rx.cond(
                    ContactState.enviado,
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "¡Tu mensaje se ha enviado correctamente! "
                                "Muchas gracias por escribirme. "
                                "Te responderé lo antes posible.",
                                color="#0f766e",
                                font_weight="600",
                            ),
                            background_color="#ecfdf5",
                            border="1px solid rgba(16, 185, 129, 0.25)",
                            border_radius="16px",
                            padding="0.85rem 1rem",
                            width="100%",
                        ),
                        rx.button(
                            "Enviar otro mensaje",
                            type="button",
                            on_click=ContactState.reset_form,
                            background_color="#1e2f5d",
                            color="#f2f2f6",
                            border_radius="16px",
                            padding_x="1.25rem",
                            padding_y="0.75rem",
                            font_weight="600",
                            _hover={
                                "background_color": "#234a73",
                                "transform": "translateY(-1px)",
                            },
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    campos_formulario,
                ),
            ),
            on_submit=ContactState.handle_submit,
            width="100%",
        ),
        width="100%",
        max_width="620px",
        flex_basis=["100%", "100%", "58%"],
        min_width="0",
        background_color="rgba(255,255,255,0.82)",
        border="1px solid rgba(30, 47, 93, 0.08)",
        border_radius="24px",
        padding=["1.1rem", "1.5rem", "2rem"],
        box_shadow="0 18px 50px rgba(17, 24, 39, 0.08)",
    )
