import flet as ft

class AppView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Generador de Contraseñas"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.theme_mode = ft.ThemeMode.DARK

        self.password_length_input = ft.TextField(label="Longitud de la contraseña", width=200)
        self.generate_button = ft.FilledButton("Generar Contraseña")
        self.password_output = ft.Text(value="", size=20)

    def get_password_length(self) -> int:
        value = (self.password_length_input.value or "").strip()
        if not value:
            raise ValueError("Introduce la longitud de la contraseña.")

        try:
            return int(value)
        except ValueError as error:
            raise ValueError("La longitud debe ser un número entero.") from error

    def show_password(self, password: str) -> None:
        self.password_length_input.error_text = None
        self.password_output.value = password
        self.page.update()

    def show_error(self, message: str) -> None:
        self.password_output.value = ""
        self.password_length_input.error_text = message
        self.page.update()

    def build_ui(self):
        self.page.add(
            self.password_length_input,
            self.generate_button,
            self.password_output
        )
