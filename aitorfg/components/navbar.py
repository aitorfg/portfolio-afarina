import reflex as rx
from aitorfg.styles import MAX_W, TEXT_STRONG, TEXT_MUTED, badge

def nav_link(label: str, href: str) -> rx.Component:
    return rx.link(
        label,
        href=href,
        color=TEXT_MUTED,
        font_weight="600",
        _hover={"color": TEXT_STRONG},
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.text("Aitor", color=TEXT_STRONG, font_weight="800", font_size="1.05em"),
                badge("Senior Data Engineer"),
                spacing="3",
                align_items="center",
            ),
            rx.spacer(),
            rx.color_mode.button(),
            rx.hstack(
                nav_link("Inicio", "/"),
                nav_link("Sobre mí", "/about"),
                nav_link("Proyectos", "/projects"),
                nav_link("Contacto", "/contact"),
                spacing="5",
                display=["none", "none", "flex"],
            ),
            spacing="3",
            width="100%",
            max_width=MAX_W,
            margin="0 auto",
            padding_x=["16px", "20px", "24px"],
            padding_y="14px",
        ),
        position="sticky",
        top="0",
        z_index="999",
        backdrop_filter="blur(12px)",
        bg="rgba(2,6,23,0.55)",
        border_bottom="1px solid rgba(255,255,255,0.08)",
        

    )
