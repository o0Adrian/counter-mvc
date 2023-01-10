from flet_mvc import FletView
import flet as ft

# view
class MainView(FletView):
    def __init__(self, controller, model):
        view = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=controller.minus_click),
                ft.TextField(
                    model.TextNumber,
                    text_align=ft.TextAlign.CENTER,
                    width=100,
                ),
                ft.IconButton(ft.icons.ADD, on_click=controller.plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        super().__init__(model, view, controller)
        