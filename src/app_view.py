import flet as ft

class AppView:

    def __init__(self, page: ft.Page):
        """Inicializa la interfaz de usuario, los controles y su disposición."""
        self.page = page
        self.page.title = "Generador de Contraseñas"
        self.page.theme_mode = ft.ThemeMode.DARK

        self.uppercase_switch = ft.Switch(label="Incluir mayúsculas", value=False)
        self.numbers_switch = ft.Switch(label="Incluir números", value=False)
        self.symbols_switch = ft.Switch(label="Incluir símbolos", value=False)

        self.password_output = ft.TextField(value="",
                                            label="Contraseña Generada",
                                            text_style=ft.TextStyle(size=32, weight=ft.FontWeight.BOLD, font_family="Courier New"),
                                            text_align=ft.TextAlign.CENTER,
                                            expand=True,
                                            read_only=True)

        self.length_slider = ft.Slider(min=8, max=32, value=12, divisions=24, label="{value}")
        
        self.generate_button = ft.FilledButton("Generar Contraseña", on_click=None)

    def get_password_length(self) -> int:
        return int(self.length_slider.value)

    def get_include_uppercase(self) -> bool:
        return self.uppercase_switch.value

    def get_include_numbers(self) -> bool:
        return self.numbers_switch.value

    def get_include_symbols(self) -> bool:
        return self.symbols_switch.value

    def show_password(self, password: str) -> None:
        self.password_output.value = password
        self.page.update()

    def show_error(self, message: str) -> None:
        self.password_output.value = ""
        self.length_slider.error_text = message
        self.page.update()

    def build_ui(self):
        self.page.add(
            ft.SafeArea(
                ft.Column(
                    [
                        ft.Text("Generador de Contraseñas", size=30, weight=ft.FontWeight.BOLD),
                        self.password_output,
                        ft.Column(
                        [
                            ft.Text("Opciones de Generación", size=20, weight=ft.FontWeight.BOLD),
                            self.uppercase_switch,
                            self.numbers_switch,
                            self.symbols_switch
                        ],
                        expand=True,
                    ),
                    ft.Text("Longitud de la Contraseña: 12", size=20, weight=ft.FontWeight.BOLD),
                    self.length_slider,
                    self.generate_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    expand=True
                ),
                expand=True
            )
        )
