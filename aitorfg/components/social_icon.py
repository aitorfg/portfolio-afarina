import reflex as rx

def social_icon(icon: str, href: str, label: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=icon,
            height="22px",
            width="22px",
            alt=label,
            opacity="0.85",
            transition="opacity 200ms ease",
            _hover={"opacity": "1"},
        ),
        href=href,
        is_external=True,
        aria_label=label,
    )
