import reflex as rx
from aitorfg.components.navbar import navbar
from aitorfg.styles_theme import (
    PAGE_BG,
    page_container,
    section_title,
    card,
    badge,
    primary_button,
    secondary_button,
    TEXT_MUTED,
    TEXT_SOFT,
    TEXT_STRONG,
)

# ---------- Small components ----------

def metric(value: str, label: str) -> rx.Component:
    return card(
        rx.text(value, font_size="1.7em", font_weight="800", color=TEXT_STRONG),
        rx.text(label, color=TEXT_MUTED, font_size="0.95em"),
        width="100%",
    )

def value_card(title: str, desc: str) -> rx.Component:
    return card(
        rx.text(title, font_weight="800", color=TEXT_STRONG),
        rx.text(desc, color=TEXT_MUTED, line_height="1.7", margin_top="6px"),
        width="100%",
    )

# ---------- Page ----------

def home() -> rx.Component:
    return rx.box(
        navbar(),

        rx.box(
            page_container(

                # ===== HERO =====
                rx.vstack(
                    rx.hstack(
                        badge("Automation"),
                        badge("Cloud-Native (GCP)"),
                        badge("Event-Driven"),
                        badge("Applied AI"),
                        spacing="2",
                        flex_wrap="wrap",
                        justify="start",
                        width="100%",
                    ),

                    rx.heading(
                        "Automatizo procesos de negocio con cloud e IA aplicada",
                        size="9",
                        color=TEXT_STRONG,
                        letter_spacing="-0.03em",
                        line_height="1.05",
                        max_width="900px",
                    ),

                    rx.text(
                        "Diseño sistemas cloud-native en Google Cloud que eliminan tareas manuales, "
                        "integran CRM y ERP, y escalan operaciones reales mediante automatización e IA.",
                        color=TEXT_SOFT,
                        font_size="1.15em",
                        line_height="1.75",
                        max_width="900px",
                    ),

                    rx.hstack(
                        primary_button("Ver proyectos", "/projects"),
                        secondary_button("Contactar", "/contact"),
                        spacing="3",
                        flex_wrap="wrap",
                    ),

                    spacing="5",
                    align="start",
                    padding_top=["32px", "40px", "56px"],
                ),

                rx.box(height="36px"),

                # ===== METRICS =====
                rx.grid(
                    metric("+750 h/año", "ahorradas mediante automatización"),
                    metric("+500", "procesos mensuales automatizados"),
                    metric("4", "personas lideradas técnicamente"),
                    template_columns=["1fr", "1fr", "1fr"],
                    gap="16px",
                    width="100%",
                ),

                rx.box(height="44px"),

                # ===== VALUE =====
                section_title(
                    "Qué hago",
                    "Trabajo como nexo entre negocio y tecnología, convirtiendo problemas operativos en sistemas automatizados y escalables.",
                ),

                rx.box(height="16px"),

                rx.grid(
                    value_card(
                        "Automatización de procesos end-to-end",
                        "Elimino tareas manuales conectando sistemas, reglas de negocio y flujos asíncronos con impacto medible.",
                    ),
                    value_card(
                        "Arquitecturas cloud-native en GCP",
                        "Diseño sistemas orientados a eventos con Cloud Run, Pub/Sub y servicios gestionados para escalar sin fricción.",
                    ),
                    value_card(
                        "Applied AI en producción",
                        "Aplico LLMs y agentes para automatizar flujos reales (OCR, clasificación, enriquecimiento y soporte a negocio).",
                    ),
                    template_columns=["1fr", "1fr", "1fr"],
                    gap="16px",
                    width="100%",
                ),

                rx.box(height="44px"),

                # ===== HOW I WORK =====
                section_title(
                    "Cómo trabajo",
                    "Ownership técnico completo, desde el diseño hasta el despliegue y la operación.",
                ),

                rx.box(height="16px"),

                card(
                    rx.vstack(
                        rx.text(
                            "Defino la arquitectura, priorizo técnicamente y acompaño la ejecución. "
                            "Traduzco necesidades de negocio en soluciones técnicas robustas, "
                            "manteniendo foco en impacto, simplicidad y mantenibilidad.",
                            color=TEXT_MUTED,
                            line_height="1.8",
                        ),
                        rx.text(
                            "Trabajo con equipos pequeños, despliegues continuos y feedback rápido, "
                            "buscando siempre soluciones pragmáticas que funcionen en producción.",
                            color=TEXT_MUTED,
                            line_height="1.8",
                        ),
                        spacing="3",
                        align="start",
                    )
                ),

                rx.box(height="44px"),

                # ===== CTA =====
                card(
                    rx.hstack(
                        rx.vstack(
                            rx.text(
                                "¿Hablamos?",
                                font_weight="800",
                                font_size="1.2em",
                                color=TEXT_STRONG,
                            ),
                            rx.text(
                                "Abierto a oportunidades remote-first y colaboraciones freelance "
                                "relacionadas con automatización, cloud y Applied AI.",
                                color=TEXT_MUTED,
                                line_height="1.6",
                            ),
                            spacing="2",
                            align="start",
                        ),
                        rx.spacer(),
                        primary_button("Contactar", "/contact"),
                        align="center",
                        flex_wrap="wrap",
                    )
                ),

            ),
            width="100%",
        ),

        bg=PAGE_BG,
        min_height="100vh",
    )
