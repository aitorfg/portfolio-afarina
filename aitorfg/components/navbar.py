import reflex as rx
from aitorfg.styles import MAX_W, TEXT_STRONG, TEXT_MUTED, badge

class NavState(rx.State):
    mobile_open: bool = False

    def toggle(self):
        self.mobile_open = not self.mobile_open


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
                rx.link(
                    rx.image(
                        src="/logo_afarina.png",
                        height="90px",
                        width="90px",
                    ),href="/",
                    # rx.text(
                    #     "Aitor Fariña",
                    #     font_weight="800",
                    #     font_size="1.05em",
                    # ),
                    # spacing="3",
                    # align="center",
                ),
                
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
            rx.icon_button(
                rx.icon("menu"),
                on_click=NavState.toggle,
                display=["flex", "flex", "none"],  # 👈 solo móvil
                variant="ghost",
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
