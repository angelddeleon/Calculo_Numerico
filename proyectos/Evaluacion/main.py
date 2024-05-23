from GaussSeidel.frontGauss import gauss
from traductor.frontTrad import frontTraductor


import flet as ft


def main(page: ft.Page):

    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.bgcolor = ft.colors.INDIGO_900
    page.update()

    def click_gauss(e):
        page.clean()
        gauss(page)

    def click_traductor(e):
        page.clean()
        frontTraductor(page)


    page.add(
        ft.Row(
            [
                ft.Text("Evaluacion #1", size=30, color=ft.colors.WHITE)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),

        ft.Row(
            [
                ft.FilledButton(
                    "Traductor Numerico",
                    style=ft.ButtonStyle(padding=20),
                    on_click= click_traductor
                ),
                ft.FilledButton(
                    "Gauss Seidel",
                    style=ft.ButtonStyle(padding=20),
                    on_click=click_gauss
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)