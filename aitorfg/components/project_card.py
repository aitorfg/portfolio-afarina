import reflex as rx

def project_card(project: dict):
    return rx.box(
        rx.heading(project["title"], size="5"),
        rx.text(project["description"]),
        rx.text(project["stack"], font_size="0.8em", color="gray"),
        padding="1.5em",
        border="1px solid #eaeaea",
        border_radius="8px",
    )
