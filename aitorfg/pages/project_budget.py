import reflex as rx
from ..components.navbar import navbar
from ..components.case_study import case_study
from aitorfg.styles_theme import PAGE_BG, page_container

def project_budget() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            page_container(
                case_study(
                    title="Automatización de Presupuestos (Iberdrola / Concesionarios)",
                    subtitle="Arquitectura event-driven para generar presupuestos automáticamente y sincronizar CRM/ERP con trazabilidad.",
                    problem="La creación de presupuestos dependía de tareas manuales y reglas complejas, generando cuellos de botella, errores y baja escalabilidad.",
                    solution="Diseñé un backend en GCP orientado a eventos: el CRM dispara el flujo, se procesan reglas de cálculo y se integra con el ERP. Se usa mensajería para absorber picos y desacoplar componentes.",
                    impact=["+750 horas/año ahorradas", "Reducción de errores humanos", "Escalado del proceso sin aumentar carga operativa"],
                    stack=["Python", "Cloud Run", "Pub/Sub", "HubSpot", "Odoo"],
                )
            ),
            width="100%",
        ),
        bg=PAGE_BG,
        min_height="100vh",
    )
