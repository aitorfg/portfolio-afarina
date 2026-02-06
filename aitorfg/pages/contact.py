import reflex as rx
from ..components.navbar import navbar
from ..styles_theme import PAGE_BG, page_container, section_title, card, TEXT_MUTED, TEXT_STRONG, primary_button, secondary_button, badge

def contact_item(label: str, value: str, href: str | None = None) -> rx.Component:
    content = rx.hstack(
        rx.text(label, color=TEXT_MUTED, width="120px"),
        rx.text(value, color=TEXT_STRONG, font_weight="700"),
        spacing="3",
        align="center",
        width="100%",
    )
    return rx.cond(
        href is None,
        content,
        rx.link(content, href=href, is_external=True, _hover={"opacity": "0.95"}),
    )

def contact() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            page_container(
                section_title(
                    "Contacto",
                    "Si quieres hablar de automatización, datos o IA aplicada en procesos reales, escríbeme.",
                ),
                rx.box(height="18px"),

                card(
                    rx.vstack(
                        rx.hstack(
                            badge("Disponible para oportunidades"),
                            rx.text("España · Remoto", color=TEXT_MUTED),
                            spacing="3",
                            align="center",
                            justify="start",
                            width="100%",
                        ),
                        rx.divider(border_color="rgba(255,255,255,0.10)"),

                        contact_item("Email", "hola@afarina.dev", "mailto:hola@afarina.dev"),
                        contact_item("LinkedIn", "linkedin.com/in/afagon", "https://www.linkedin.com/in/afagon"),
                        contact_item("GitHub", "github.com/aitorfg", "https://github.com/aitorfg"),

                        rx.divider(border_color="rgba(255,255,255,0.10)"),

                        rx.hstack(
                            primary_button("Ver proyectos", "/projects"),
                            secondary_button("Sobre mí", "/about"),
                            spacing="3",
                            flex_wrap="wrap",
                        ),
                        spacing="4",
                        align="start",
                    )
                ),
            ),
            width="100%",
        ),
        bg=PAGE_BG,
        min_height="100vh",
    )
