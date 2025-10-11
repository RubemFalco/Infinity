#TERMINAL    
#  python -m venv venv  ----> cria o ambiente virtual
#  venv/scripts/activate ----> ativa o ambiente virtual
#  pip install flet ----> instala a biblioteca "flet"
#  abrir o flet.dev e copiar o primeiro código apresentado na página "docs"
#  colar o código no editor de código-fonte(em meu caso, VS CODE) ---->
import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)
#  Terminal
#  python nome_do_documento ----> Roda o programa em Python
