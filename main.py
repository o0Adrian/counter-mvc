import flet as ft
from mvc.controller import Controller
from mvc.view import MainView
from mvc.model import Model

def main(page: ft.Page):
    # MVC set-up
    model = Model()
    controller = Controller(page, model)
    view = MainView(controller, model)
    
    # Settings
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Run
    page.add(
        *view.content
    )

ft.app(target=main)
