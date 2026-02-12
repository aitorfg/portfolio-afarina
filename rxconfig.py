import reflex as rx

config = rx.Config(
    app_name="aitorfg",
    title="Aitor Fariña · Automation & Cloud Engineer",
    favicon="/favicon.ico",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)