import reflex as rx

from .pages.home import home
from .pages.projects import projects
from .pages.about import about
from .pages.contact import contact
from .pages.cv import cv


from .pages.project_budget import project_budget  # 👈 case study

from .components.global_css import global_css

app = rx.App()
app.add_page(lambda: rx.fragment(global_css(), home()), route="/")
app.add_page(projects, route="/projects")
app.add_page(about, route="/about")
app.add_page(contact, route="/contact")
app.add_page(project_budget, route="/projects/budget")
app.add_page(cv, route="/cv")