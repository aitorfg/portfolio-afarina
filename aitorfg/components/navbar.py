import reflex as rx
from aitorfg.styles import MAX_W, TEXT_STRONG, TEXT_MUTED


class NavState(rx.State):
    mobile_open: bool = False

    def toggle(self):
        self.mobile_open = not self.mobile_open

    def close(self):
        self.mobile_open = False


def nav_link(label: str, href: str, on_click=None) -> rx.Component:
    return rx.link(
        label,
        href=href,
        on_click=on_click,
        color=TEXT_MUTED,
        font_weight="600",
        _hover={"color": TEXT_STRONG},
    )


def navbar() -> rx.Component:
    return rx.box(
        # ===== TOP BAR =====
        rx.box(
            rx.hstack(
                # Logo
                rx.link(
                    rx.image(
                        src="/logo_afarina.png",
                        height="90px",
                        width="90px",
                    ),
                    href="/",
                    on_click=NavState.close,
                ),

                rx.spacer(),

                # Right side controls
                rx.hstack(
                    # Desktop links
                    rx.hstack(
                        nav_link("Inicio", "/"),
                        nav_link("Sobre mí", "/about"),
                        nav_link("Proyectos", "/projects"),
                        nav_link("Contacto", "/contact"),
                        spacing="5",
                        display=["none", "none", "flex"],  # desktop only
                    ),

                    # Color mode toggle (always visible)
                    rx.color_mode.button(),

                    # Mobile hamburger (mobile only)
                    rx.icon_button(
                        rx.icon("menu"),
                        on_click=NavState.toggle,
                        variant="ghost",
                        display=["flex", "flex", "none"],  # mobile only
                    ),

                    spacing="3",
                    align="center",
                ),

                spacing="3",
                width="100%",
                max_width=MAX_W,
                margin="0 auto",
                padding_x=["16px", "20px", "24px"],
                padding_y="14px",
                align="center",
            ),
            backdrop_filter="blur(12px)",
            bg="rgba(2,6,23,0.55)",
            border_bottom="1px solid rgba(255,255,255,0.08)",
        ),

        # ===== MOBILE DROPDOWN =====
        rx.cond(
            NavState.mobile_open,
            rx.box(
                rx.vstack(
                    nav_link("Inicio", "/", on_click=NavState.close),
                    nav_link("Sobre mí", "/about", on_click=NavState.close),
                    nav_link("Proyectos", "/projects", on_click=NavState.close),
                    nav_link("Contacto", "/contact", on_click=NavState.close),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
                width="100%",
                border_bottom="1px solid rgba(255,255,255,0.08)",
                bg="rgba(2,6,23,0.92)",
                backdrop_filter="blur(12px)",
                padding_y="12px",
            ),
        ),

        position="sticky",
        top="0",
        z_index="999",
        width="100%",
    )
