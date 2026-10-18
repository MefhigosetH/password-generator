import flet as ft
from app_model import AppModel
from app_view import AppView
from app_controller import AppController

def main(page: ft.Page):
    navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.INFO, label="Ayuda"),
        ],
        selected_index=0,
        on_change=lambda e: print(f"Selected index: {e.control.selected_index}"),
    )

    model = AppModel()
    view = AppView(page)
    controller = AppController(model, view)

    view.build_ui()
    controller.handle_generate({})

    page.add(navigation_bar)

if __name__ == "__main__":
    ft.run(main)