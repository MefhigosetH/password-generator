
import flet as ft
from app.views.layouts.main_layout import MainLayout
from app.controllers.help_controller import HelpController
from flet import UrlLauncher

class HelpView:
    def __init__(self, page, router):
        self.page = page
        self.router = router
        self.controller = HelpController()
        self.url_launcher = UrlLauncher()
    
    async def open_docs(self, e):
        await self.url_launcher.launch_url("https://github.com/mefhigoseth/Fleting")

    async def open_issues(self, e):
        await self.url_launcher.launch_url("https://github.com/alexyucra/fleting/issues")

    async def open_support(self, e):
        await self.url_launcher.launch_url("https://alexyucra.github.io/#contato")

    def render(self):
        

        content = ft.Column(
            spacing=24,
            controls=[
                ft.Image(
                    src="icon.png",
                    width=144
                ),
                ft.Text(
                    "Generador de contraseñas",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    "Generador de contraseñas aleatorias para móviles. "
                    "Seguro, transparante y de código fuente abierto.",
                    size=18,
                    weight=ft.FontWeight.W_500,
                ),

                ft.Text(
                    "Desarrollado por Victor Villarreal <mefhigoseth@gmail.com>",
                    color=ft.Colors.GREY_600,
                ),

                ft.Divider(),

                ft.Button(
                    "Documentación oficial",
                    icon=ft.Icons.CODE,
                    on_click=self.open_docs,
                ),

                ft.Button(
                    "Reportar un problema",
                    icon=ft.Icons.BUG_REPORT,
                    on_click=self.open_issues,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        return MainLayout(
            page=self.page,
            content=content,
            router=self.router,
        )
