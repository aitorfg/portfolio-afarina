import reflex as rx
from aitorfg.components.navbar import navbar
from aitorfg.styles import (
    PAGE_BG, page_container, section_title, card,
    TEXT_STRONG, TEXT_SOFT, TEXT_MUTED, badge,
    primary_button, secondary_button
)

def metric(value: str, label: str) -> rx.Component:
    return card(
        rx.text(value, color=TEXT_STRONG, font_size="1.6em", font_weight="800"),
        rx.text(label, color=TEXT_MUTED, font_size="0.95em"),
        width="100%",
    )

def feature(title: str, desc: str) -> rx.Component:
    return card(
        rx.text(title, color=TEXT_STRONG, font_weight="750"),
        rx.text(desc, color=TEXT_MUTED, line_height="1.6", margin_top="6px"),
        width="100%",
    )

def home() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            page_container(
                # HERO
                rx.vstack(
                    rx.hstack(
                        badge("GCP · Event-Driven · Automation"),
                        badge("Applied AI (Gemini · LangChain · LangGraph)"),
                        spacing="2",
                        flex_wrap="wrap",
                        justify="start",
                        width="100%",
                    ),
                    rx.heading(
                        "Automatizo procesos de negocio con datos, cloud e IA aplicada.",
                        size="9",
                        color=TEXT_STRONG,
                        letter_spacing="-0.03em",
                        line_height="1.05",
                    ),
                    rx.text(
                        "Diseño sistemas en producción en Google Cloud (Cloud Run, Pub/Sub, BigQuery) "
                        "que eliminan procesos manuales, integran CRM/ERP y escalan operaciones.",
                        color=TEXT_SOFT,
                        font_size="1.15em",
                        line_height="1.7",
                        max_width="900px",
                    ),
                    rx.hstack(
                        primary_button("Ver proyectos", "/projects"),
                        secondary_button("Contacto", "/contact"),
                        spacing="3",
                        flex_wrap="wrap",
                    ),
                    spacing="5",
                    align_items="flex-start",
                    padding_top=["26px", "34px", "46px"],
                    class_name="fade-up"
                ),

                rx.box(height="28px"),

                # METRICS
                rx.grid(
                    metric("+750", "horas/año ahorradas (automatización)"),
                    metric("+500", "procesos mensuales automatizados"),
                    metric("4", "personas a cargo (liderazgo técnico)"),
                    template_columns=["1fr", "1fr", "1fr"],
                    gap="16px",
                    width="100%",
                ),

                rx.box(height="34px"),

                # VALUE
                section_title(
                    "Qué hago",
                    "Trabajo como nexo negocio ↔ tecnología: convierto problemas operativos en soluciones técnicas escalables.",
                ),
                rx.box(height="14px"),
                rx.grid(
                    feature("Arquitecturas cloud en GCP", "Event-driven, colas, orquestación y despliegues CI/CD para procesos críticos."),
                    feature("Integraciones CRM/ERP/Partners", "HubSpot, Odoo, APIs seguras y flujos desacoplados para absorber picos."),
                    feature("Automatización web cuando no hay API", "Scraping/RPA robusto con control de errores y observabilidad básica."),
                    template_columns=["1fr", "1fr", "1fr"],
                    gap="16px",
                    width="100%",
                ),

                rx.box(height="34px"),

                # CTA
                card(
                    rx.hstack(
                        rx.vstack(
                            rx.text("¿Hablamos?", color=TEXT_STRONG, font_weight="800", font_size="1.2em"),
                            rx.text(
                                "Si buscas automatizar procesos, mejorar tu plataforma de datos o aplicar IA en operaciones, te puedo ayudar.",
                                color=TEXT_MUTED,
                                line_height="1.6",
                            ),
                            spacing="2",
                            align_items="flex-start",
                        ),
                        rx.spacer(),
                        primary_button("Contactar", "/contact"),
                        align_items="center",
                        flex_wrap="wrap",
                    ),
                ),
            ),
            width="100%",
        ),
        bg=PAGE_BG,
        min_height="100vh",
    )
