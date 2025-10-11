import flet as ft


def main(page: ft.Page):
    page.add(
        ft.AutofillGroup(
            ft.Column(
                controls=[
                    ft.TextField(
                        label="Nome",
                        autofill_hints=ft.AutofillHint.NAME,
                    ),
                    ft.TextField(
                        label="Email",
                        autofill_hints=[ft.AutofillHint.EMAIL],
                    ),
                    ft.TextField(
                        label="Número de Telefone",
                        autofill_hints=[ft.AutofillHint.TELEPHONE_NUMBER],
                    ),
                    ft.TextField(
                        label="Endereço",
                        autofill_hints=ft.AutofillHint.FULL_STREET_ADDRESS,
                    ),
                    ft.TextField(
                        label="Trabalho Atual",
                        autofill_hints=ft.AutofillHint.POSTAL_CODE,
                    ),
                ]
            )
        )
    )


# run with 'flet run -w'
ft.app(main)