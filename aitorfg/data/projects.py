PROJECTS = [
    {
        "title": "Automatización de Presupuestos (Iberdrola / Concesionarios)",
        "tag": "Event-driven · CRM → ERP",
        "description": "Generación automática de presupuestos con arquitectura orientada a eventos y trazabilidad entre sistemas.",
        "stack": ["Python", "Cloud Run", "Pub/Sub", "HubSpot", "Odoo"],
        "route": "/projects/budget",
    },
    {
        "title": "Lightbill: Extracción y Enriquecimiento de Facturas Eléctricas",
        "tag": "Automation · Data pipeline",
        "description": "Pipeline asíncrono para extracción y consolidación de datos de consumo eléctrico y actualización near-real-time en CRM.",
        "stack": ["Python", "Pub/Sub", "Cloud Run", "Firestore", "Selenium", "Gemini API"],
        "route": "/projects/lightbill",
    },
    {
        "title": "Ingesta de Leads de Partners (API Gateway + HubSpot)",
        "tag": "API · Security",
        "description": "API segura para ingesta automatizada de leads externos con control de acceso y backend desacoplado.",
        "stack": ["API Gateway", "Cloud Run", "HubSpot"],
        "route": "/projects/partners",
    },
    {
        "title": "Plataforma de Datos y Analytics",
        "tag": "BigQuery · Dashboards",
        "description": "Pipelines ETL a BigQuery y dashboards operativos con Looker/Dash para reporting y control de negocio.",
        "stack": ["BigQuery", "Cloud Storage", "Scheduler", "Looker", "Dash"],
        "route": "/projects/analytics",
    },
    {
        "title": "Automatización Web sin APIs",
        "tag": "Scraping · Robustness",
        "description": "Extracción controlada desde portales sin API, con control de errores y reintentos.",
        "stack": ["Python", "Selenium", "Proxies", "GCP"],
        "route": "/projects/automation-web",
    },
]
