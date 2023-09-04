import reflex as rx
from chatReflex import style


def index() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.vstack(
                rx.text(
                    "MI EMPRENDIMIENTO",
                    font_size="25px"
                ),
            ),
            bg="lightgreen",
            width="100%",
        ),
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.button(
                        "INICIO",
                    ),
                    rx.button(
                        "CATALOGO",
                    ),
                    rx.button(
                        "CONTACTO",
                    ),
                ),
                rx.image(
                    src="/banner.jpeg", width="500px", height="auto"
                ),
                bg="lightgreen",
                padding="3px",
                width="100%",
            ),
            bg="lightgreen",
            width="100%",
        ),
        width="100%",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
