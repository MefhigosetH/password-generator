import flet as ft
from app_model import AppModel
from app_view import AppView
from app_controller import AppController

def main(page: ft.Page):
    model = AppModel()
    view = AppView(page)
    AppController(model, view)

    view.build_ui()

if __name__ == "__main__":
    ft.run(main)