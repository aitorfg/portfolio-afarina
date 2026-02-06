import reflex as rx
from ..styles_theme import card, section_title, TEXT_MUTED, TEXT_STRONG, badge

def case_study(
    title: str,
    subtitle: str,
    problem: str,
    solution: str,
    impact: list[str],
    stack: list[str],
) -> rx.Component:
    def chip(s: str) -> rx.Component:
        return rx.box(
            s,
            padding_x="10px",
            padding_y="6px",
            border_radius="999px",
            bg="rgba(255,255,255,0.06)",
            border="1px solid rgba(255,255,255,0.14)",
            color=TEXT_STRONG,
            font_size="0.85em",
            font_weight="650",
        )

    return rx.vstack(
        rx.hstack(badge("Case study"), spacing="2"),
        rx.heading(
            title,
            size="8",
            color=TEXT_STRONG,
            letter_spacing="-0.03em",
            line_height="1.05",
        ),
        rx.text(subtitle, color=TEXT_MUTED, font_size="1.05em", line_height="1.7"),
        rx.box(height="18px"),

        section_title("Problema", None),
        card(rx.text(problem, color=TEXT_MUTED, line_height="1.8")),

        section_title("Solución", None),
        card(rx.text(solution, color=TEXT_MUTED, line_height="1.8")),

        section_title("Impacto", None),
        card(rx.vstack(*[rx.text(f"• {x}", color=TEXT_MUTED) for x in impact], spacing="2")),

        section_title("Stack", None),
        card(
            rx.hstack(*[chip(s) for s in stack], spacing="2", flex_wrap="wrap")
        ),

        spacing="4",
        align_items="flex-start",
        width="100%",
    )
