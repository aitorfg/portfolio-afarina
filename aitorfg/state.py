# my_portfolio/constants.py

NAV_ITEMS = [
    {"label": "Proyectos", "href": "#projects"},
    {"label": "Sobre mí", "href": "#about"},
    {"label": "Contacto", "href": "#contact"},
]

HERO = {
    "badge": "Aitor Fariña · Data & Automation Engineer (GCP)",
    "headline": "Pipelines y automatizaciones de datos listas para producción.",
    "subheadline": "Diseño y despliego sistemas en Python y Google Cloud que convierten datos en procesos automatizados y dashboards fiables.",
    "proof": [
        "Sistemas robustos con foco en fiabilidad, coste y escalabilidad.",
        "ETLs incrementales, idempotencia, logging, retries y alertas.",
        "Integraciones API y dashboards conectados a datos reales.",
    ],
    "stack": ["Python", "GCP", "BigQuery", "Cloud Run", "Docker", "APIs", "Dashboards"],
}

PROJECTS = [
    {
        "title": "Observatorio inmobiliario (INE + idealista)",
        "desc": "ETL diario + modelo de datos + dashboard para analizar accesibilidad y tendencias por zona.",
        "stack": ["Python", "BigQuery", "Cloud Run", "Scheduler"],
    },
    {
        "title": "Integraciones CRM/ERP automatizadas",
        "desc": "Sincronización y enriquecimiento de datos vía APIs con control de calidad y reintentos.",
        "stack": ["Python", "FastAPI", "APIs", "Docker"],
    },
    {
        "title": "Monitorización de automatizaciones",
        "desc": "Observabilidad, alertas y métricas para jobs en producción.",
        "stack": ["Logging", "Alerts", "Cloud Monitoring"],
    },
]
