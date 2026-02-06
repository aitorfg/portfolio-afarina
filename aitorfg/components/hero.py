import reflex as rx

def hero():
    return rx.vstack(
        rx.heading(
            "Automatizo procesos de negocio con datos, cloud e IA aplicada",
            size="8",
        ),
        rx.text(
            "Senior Data Engineer especializado en Google Cloud, "
            "arquitecturas event-driven y automatización end-to-end.",
            font_size="1.2em",
            color="gray",
        ),
        rx.hstack(
            rx.button("Ver proyectos", on_click=rx.redirect("/projects")),
            rx.button("Contacto", variant="outline", on_click=rx.redirect("/contact")),
            spacing="4",
        ),
        spacing="6",
        padding_y="6em",
        align="center",
    )
