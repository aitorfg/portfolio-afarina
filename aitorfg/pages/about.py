import reflex as rx
from ..components.navbar import navbar
from ..styles_theme import (
    PAGE_BG,
    page_container,
    section_title,
    card,
    badge,
    TEXT_MUTED,
    TEXT_STRONG,
)

def about() -> rx.Component:
    return rx.box(
        navbar(),

        rx.box(
            page_container(

                # ===== HEADER =====
                rx.vstack(
                    rx.hstack(
                        badge("Senior Automation & Cloud Engineer"),
                        badge("Applied AI"),
                        spacing="2",
                        flex_wrap="wrap",
                        justify="start",
                        width="100%",
                    ),

                    rx.heading(
                        "Diseño sistemas que automatizan procesos reales",
                        size="8",
                        color=TEXT_STRONG,
                        letter_spacing="-0.03em",
                        line_height="1.1",
                        max_width="900px",
                    ),

                    rx.text(
                        "Mi foco está en crear soluciones técnicas que eliminen fricción operativa, "
                        "reduzcan errores y permitan escalar negocio sin aumentar complejidad.",
                        color=TEXT_MUTED,
                        font_size="1.1em",
                        line_height="1.7",
                        max_width="900px",
                    ),

                    spacing="4",
                    align="start",
                    padding_top=["32px", "40px", "56px"],
                ),

                rx.box(height="44px"),

                # ===== WHO I AM =====
                section_title(
                    "Quién soy profesionalmente",
                    None,
                ),

                rx.box(height="16px"),

                card(
                    rx.vstack(
                        rx.text(
                            "Soy Senior Automation & Cloud Engineer con experiencia diseñando y operando "
                            "sistemas en producción que automatizan procesos críticos de negocio.",
                            color=TEXT_MUTED,
                            line_height="1.8",
                        ),
                        rx.text(
                            "Trabajo principalmente con Python y Google Cloud Platform, construyendo "
                            "arquitecturas cloud-native y orientadas a eventos que conectan CRM, ERP "
                            "y fuentes externas de datos.",
                            color=TEXT_MUTED,
                            line_height="1.8",
                        ),
                        spacing="3",
                        align="start",
                    )
                ),

                rx.box(height="44px"),

                # ===== HOW I WORK =====
                section_title(
                    "Cómo trabajo",
                    None,
                ),

                rx.box(height="16px"),

                rx.grid(
                    card(
                        rx.text("Ownership end-to-end", font_weight="800", color=TEXT_STRONG),
                        rx.text(
                            "Asumo responsabilidad completa desde el diseño hasta el despliegue "
                            "y la operación en producción.",
                            color=TEXT_MUTED,
                            line_height="1.7",
                            margin_top="6px",
                        ),
                    ),
                    card(
                        rx.text("Nexo negocio ↔ tecnología", font_weight="800", color=TEXT_STRONG),
                        rx.text(
                            "Traduzco necesidades de negocio en soluciones técnicas claras y escalables, "
                            "priorizando impacto real.",
                            color=TEXT_MUTED,
                            line_height="1.7",
                            margin_top="6px",
                        ),
                    ),
                    card(
                        rx.text("Arquitectura antes que código", font_weight="800", color=TEXT_STRONG),
                        rx.text(
                            "Defino arquitectura, flujos y decisiones clave antes de ejecutar, "
                            "evitando complejidad innecesaria.",
                            color=TEXT_MUTED,
                            line_height="1.7",
                            margin_top="6px",
                        ),
                    ),
                    template_columns=["1fr", "1fr", "1fr"],
                    gap="16px",
                    width="100%",
                ),

                rx.box(height="44px"),

                # ===== TECH & AI =====
                section_title(
                    "Automatización, cloud e IA aplicada",
                    None,
                ),

                rx.box(height="16px"),

                card(
                    rx.vstack(
                        rx.text(
                            "Mi trabajo se centra en automatización y arquitecturas cloud-native, "
                            "utilizando servicios gestionados para construir sistemas robustos y mantenibles.",
                            color=TEXT_MUTED,
                            line_height="1.8",
                        ),
                        rx.text(
                            "Actualmente estoy evolucionando hacia Applied AI, explorando el uso de "
                            "LLMs y agentes para automatizar flujos comerciales y operativos reales, "
                            "siempre con foco en impacto y viabilidad en producción.",
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
                    rx.vstack(
                        rx.text(
                            "¿En qué te puedo ayudar?",
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
                    )
                ),

            ),
            width="100%",
        ),

        bg=PAGE_BG,
        min_height="100vh",
    )
