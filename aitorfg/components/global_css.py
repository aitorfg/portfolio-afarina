import reflex as rx

def global_css() -> rx.Component:
    return rx.el.style(
        """
        @keyframes fadeUp {
          from { opacity: 0; transform: translateY(10px); }
          to   { opacity: 1; transform: translateY(0px); }
        }
        .fade-up { animation: fadeUp 600ms ease both; }
        """
    )
