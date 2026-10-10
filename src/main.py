import flet as ft
from app_model import AppModel
from app_view import AppView
from app_controller import AppController

def main(page: ft.Page):
    model = AppModel()
    view = AppView(page)
    controller = AppController(model, view)

    view.build_ui()
    controller.handle_generate({})

if __name__ == "__main__":
    ft.run(main)