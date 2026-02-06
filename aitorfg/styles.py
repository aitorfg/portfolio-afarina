import reflex as rx

# --- Design tokens ---
MAX_W = "1100px"

RADIUS = "16px"
BORDER = "1px solid rgba(255,255,255,0.10)"

PAGE_BG = "linear-gradient(180deg, rgba(15,23,42,1) 0%, rgba(2,6,23,1) 100%)"  # slate-900 → slate-950
CARD_BG = "rgba(255,255,255,0.04)"
CARD_BG_HOVER = "rgba(255,255,255,0.07)"

TEXT_MUTED = "rgba(255,255,255,0.70)"
TEXT_SOFT = "rgba(255,255,255,0.85)"
TEXT_STRONG = "rgba(255,255,255,0.96)"

ACCENT = "#60a5fa"      # blue-400
ACCENT_2 = "#a78bfa"    # violet-400

SHADOW = "0 10px 30px rgba(0,0,0,0.35)"

def page_container(*children) -> rx.Component:
    return rx.box(
        rx.box(
            *children,
            max_width=MAX_W,
            width="100%",
            margin="0 auto",
            padding_x=["16px", "20px", "24px"],
            padding_y=["24px", "28px", "36px"],
        ),
        width="100%",
    )

def section_title(title: str, subtitle: str | None = None) -> rx.Component:
    return rx.vstack(
        rx.heading(title, size="7", color=TEXT_STRONG, letter_spacing="-0.02em"),
        rx.cond(
            subtitle is not None,
            rx.text(subtitle, color=TEXT_MUTED, font_size="1.05em", line_height="1.6"),
        ),
        align_items="flex-start",
        spacing="2",
    )

def card(*children, **kwargs) -> rx.Component:
    return rx.box(
        *children,
        bg=CARD_BG,
        border=BORDER,
        border_radius=RADIUS,
        box_shadow=SHADOW,
        padding=["16px", "18px", "20px"],
        transition="all 250ms ease",
        _hover={"bg": CARD_BG_HOVER, "transform": "translateY(-2px)"},
        **kwargs,
    )

def badge(text: str) -> rx.Component:
    return rx.box(
        text,
        padding_x="10px",
        padding_y="6px",
        border_radius="999px",
        bg="rgba(96,165,250,0.12)",
        border="1px solid rgba(96,165,250,0.25)",
        color="rgba(255,255,255,0.92)",
        font_size="0.85em",
        font_weight="600",
    )

def primary_button(label: str, href: str) -> rx.Component:
    return rx.link(
        rx.button(
            label,
            bg=f"linear-gradient(90deg, {ACCENT}, {ACCENT_2})",
            color="black",
            font_weight="700",
            border_radius="12px",
            padding_x="16px",
            padding_y="12px",
            _hover={"filter": "brightness(1.05)"},
        ),
        href=href,
    )

def secondary_button(label: str, href: str) -> rx.Component:
    return rx.link(
        rx.button(
            label,
            bg="rgba(255,255,255,0.06)",
            border="1px solid rgba(255,255,255,0.16)",
            color=TEXT_STRONG,
            font_weight="650",
            border_radius="12px",
            padding_x="16px",
            padding_y="12px",
            _hover={"bg": "rgba(255,255,255,0.10)"},
        ),
        href=href,
    )
