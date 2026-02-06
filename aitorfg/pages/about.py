import reflex as rx
from ..components.navbar import navbar
from ..styles_theme import PAGE_BG, page_container, section_title, card, TEXT_MUTED, TEXT_STRONG, badge

def about() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            page_container(
                section_title(
                    "Sobre mí",
                    "Senior Data Engineer enfocado en automatización, datos y arquitecturas cloud en GCP.",
                ),
                rx.box(height="18px"),

                # Bloque principal
                card(
                    rx.vstack(
                        rx.text(
                            "Soy Senior Data Engineer con experiencia diseñando y operando sistemas en producción "
                            "que automatizan procesos críticos de negocio. Trabajo principalmente con Python y "
                            "Google Cloud Platform (Cloud Run, Pub/Sub, BigQuery).",
                            color=TEXT_MUTED,
                            line_height="1.8",
                        ),
                        rx.text(
                            "Actúo como nexo entre negocio y tecnología: traduzco problemas operativos en soluciones "
                            "técnicas escalables, asumiendo ownership end-to-end desde el diseño hasta la operación.",
                            color=TEXT_MUTED,
                            line_height="1.8",
                        ),
                        spacing="3",
                        align="start",
                    )
                ),

                rx.box(height="18px"),

                # Highlights
                section_title("En lo que más aporto", None),
                rx.box(height="12px"),
                rx.grid(
                    card(
                        rx.text("Arquitecturas event-driven", color=TEXT_STRONG, font_weight="800"),
                        rx.text(
                            "Diseño sistemas desacoplados con colas/mensajería para absorber picos y escalar procesos.",
                            color=TEXT_MUTED,
                            line_height="1.7",
                            margin_top="6px",
                        ),
                    ),
                    card(
                        rx.text("Automatización de procesos", color=TEXT_STRONG, font_weight="800"),
                        rx.text(
                            "Elimino tareas manuales, reduzco errores y mejoro eficiencia con impacto medible.",
                            color=TEXT_MUTED,
                            line_height="1.7",
                            margin_top="6px",
                        ),
                    ),
                    card(
                        rx.text("Applied AI (en evolución)", color=TEXT_STRONG, font_weight="800"),
                        rx.text(
                            "Exploro el uso de LLMs y agentes para automatización real (Gemini API, LangChain, LangGraph).",
                            color=TEXT_MUTED,
                            line_height="1.7",
                            margin_top="6px",
                        ),
                    ),
                    template_columns=["1fr", "1fr", "1fr"],
                    gap="16px",
                    width="100%",
                ),
            ),
            width="100%",
        ),
        bg=PAGE_BG,
        min_height="100vh",
    )
