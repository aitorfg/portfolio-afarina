import reflex as rx
from aitorfg.components.navbar import navbar
from aitorfg.styles import PAGE_BG, page_container, section_title, card, badge, TEXT_STRONG, TEXT_MUTED
from aitorfg.data.projects import PROJECTS

def chip(text: str) -> rx.Component:
    return rx.box(
        text,
        padding_x="10px",
        padding_y="6px",
        border_radius="999px",
        bg="rgba(255,255,255,0.06)",
        border="1px solid rgba(255,255,255,0.14)",
        color="rgba(255,255,255,0.86)",
        font_size="0.82em",
        font_weight="650",
    )

def project_card(p: dict) -> rx.Component:
    return card(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text(p["title"], color=TEXT_STRONG, font_weight="800", font_size="1.05em"),
                    rx.text(p["tag"], color=TEXT_MUTED, font_size="0.92em"),
                    spacing="1",
                    align_items="flex-start",
                ),
                rx.spacer(),
                badge("Case study"),
                width="100%",
                align_items="flex-start",
            ),
            rx.text(p["description"], color=TEXT_MUTED, line_height="1.7"),
            rx.hstack(*[chip(s) for s in p["stack"]], spacing="2", flex_wrap="wrap"),
            spacing="3",
            align_items="flex-start",
        ),
        width="100%",
    )

def projects() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            page_container(
                section_title(
                    "Proyectos",
                    "Una selección de sistemas en producción: automatización, integraciones y plataformas de datos en GCP.",
                ),
                rx.box(height="18px"),
                rx.grid(
                    *[project_card(p) for p in PROJECTS],
                    template_columns=["1fr", "1fr"],  # 2 columnas
                    gap="16px",
                    width="100%",
                ),
            ),
            width="100%",
        ),
        bg=PAGE_BG,
        min_height="100vh",
    )
