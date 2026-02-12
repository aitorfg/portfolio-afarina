import reflex as rx
from aitorfg.components.navbar import navbar
from aitorfg.styles import MAX_W, TEXT_STRONG, TEXT_MUTED

PDF_PATH = "/CV_Aitor_Fariña_González.pdf"  # debe existir en assets/


def cv() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.vstack(
                rx.heading("CV", size="8", color=TEXT_STRONG),
                rx.text(
                    "Puedes visualizarlo aquí o descargarlo directamente.",
                    color=TEXT_MUTED,
                ),
                rx.hstack(
                    rx.link(
                        rx.button("Descargar CV"),
                        href=PDF_PATH,
                        is_external=True,
                    ),
                    rx.link(
                        rx.button("Abrir en nueva pestaña", variant="soft"),
                        href=PDF_PATH,
                        is_external=True,
                    ),
                    spacing="3",
                    flex_wrap="wrap",
                ),
                rx.box(height="18px"),

                # Visor embebido
                rx.box(
                    rx.html(
                        f"""
                        <iframe
                            src="{PDF_PATH}"
                            width="100%"
                            height="920px"
                            style="
                                border: 0;
                                border-radius: 14px;
                                background: rgba(255,255,255,0.03);
                            "
                        ></iframe>
                        """
                    ),
                    width="100%",
                ),

                spacing="4",
                align="start",
                width="100%",
                max_width=MAX_W,
                margin="0 auto",
                padding_x=["16px", "20px", "24px"],
                padding_y=["24px", "32px", "40px"],
            ),
            width="100%",
        ),
        min_height="100vh",
    )
