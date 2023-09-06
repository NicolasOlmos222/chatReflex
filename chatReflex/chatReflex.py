import reflex as rx
from chatReflex import style
from chatReflex import introduccion

inicio = False
catalogo = False
contacto = False


class MyState(rx.State):
    inicioBox: str = "none"
    catalogoBox: str = "none"
    contactoBox: str = "none"
    
    def inicioBlock(self):
        self.inicioBox = "block"
        self.catalogoBox = "none"
        self.contactoBox = "none"
    def catalogoBlock(self):
        self.inicioBox = "none"
        self.catalogoBox = "block"
        self.contactoBox = "none"
    def contactoBlock(self):
        self.inicioBox = "none"
        self.catalogoBox = "none"
        self.contactoBox = "block"
        
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
                        on_click=MyState.inicioBlock(),
                    ),
                    rx.button(
                        "CATALOGO",
                        on_click=MyState.catalogoBlock(),
                    ),
                    rx.button(
                        "CONTACTO",
                        on_click=MyState.contactoBlock(),
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
        rx.box(
            rx.text(introduccion.texto1, 
                    style = style.texto_style1), 
            rx.text(introduccion.texto2, 
                    style = style.texto_style2), 
            rx.text(introduccion.texto3, 
                    style = style.texto_style1), 
            rx.text(introduccion.texto4, 
                    style = style.texto_style2), 
            rx.text(introduccion.texto5, 
                    style = style.texto_style1), 
            display=MyState.inicioBox,
        ),
        rx.grid(
            rx.grid_item(content=rx.image(url="imagen1.jpeg"), row_span=1, col_span=1),
            rx.grid_item(content=rx.image(url="imagen2.jpeg"), row_span=1, col_span=1),
            rx.grid_item(content=rx.image(url="imagen3.jpeg"), row_span=1, col_span=1),
            rx.grid_item(content=rx.image(url="imagen4.jpeg"), row_span=1, col_span=1),
            rx.grid_item(content=rx.image(url="imagen5.jpeg"), row_span=1, col_span=1),
            rx.grid_item(content=rx.image(url="imagen6.jpeg"), row_span=1, col_span=1),
            rx.grid_item(content=rx.image(url="imagen7.jpeg"), row_span=1, col_span=1),
            rx.grid_item(content=rx.image(url="imagen8.jpeg"), row_span=1, col_span=1),
            rx.grid_item(content=rx.image(url="imagen9.jpeg"), row_span=1, col_span=1),
            template_columns="repeat(3, 1fr)",
            template_rows="repeat(3, 1fr)",
            gap=4,
            display=MyState.catalogoBox,
        ), 
        
        rx.box(
            rx.text("CONTACTO"), 
            display=MyState.contactoBox,
        ),
        width="100%",
    )

app = rx.App()
app.add_page(index)
app.compile()
