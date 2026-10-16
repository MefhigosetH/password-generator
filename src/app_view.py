import flet as ft

class AppView:

    def __init__(self, page: ft.Page):
        """Inicializa la interfaz de usuario, los controles y su disposición."""
        self.page = page
        self.page.title = "Generador de Contraseñas"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.padding = 20

        self.uppercase_switch = ft.Switch(value=False, active_color=ft.Colors.BLUE_400)
        self.numbers_switch = ft.Switch(value=False, active_color=ft.Colors.BLUE_400)
        self.symbols_switch = ft.Switch(value=False, active_color=ft.Colors.BLUE_400)

        self.password_output = ft.TextField(value="",
                                            border=ft.NoInputBorder(),
                                            text_style=ft.TextStyle(
                                                font_family="monospace", 
                                                size=28,
                                                color=ft.Colors.ON_SECONDARY_CONTAINER,
                                                weight=ft.FontWeight.BOLD
                                            ),
                                            read_only=True,
                                            multiline=True,
                                            expand=True,)

        self.length_slider = ft.Slider(min=8, max=32, value=12, divisions=24, label="{value}", active_color=ft.Colors.BLUE_400, inactive_color=ft.Colors.GREY_800,)
        self.txt_length_number = ft.Text(str(self.length_slider.value), weight=ft.FontWeight.BOLD, size=16, color=ft.Colors.BLUE_400)
        self.strength_bar = ft.ProgressBar(value=0, color=ft.Colors.GREY_500, bgcolor=ft.Colors.GREY_800, expand=True)
        self.strength_text = ft.Text("Seguridad: Sin evaluar", size=12, color=ft.Colors.GREY_400)
        self.generate_button = ft.FilledButton(
                                    content="Generar Contraseña",
                                    icon=ft.Icons.AUTO_AWESOME,
                                    color=ft.Colors.WHITE,
                                    bgcolor=ft.Colors.BLUE_600,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        padding=20
                                    ),
                                    width=600,
                                )
        self.refresh_button = ft.FilledButton(icon=ft.Icons.REFRESH, content="Generar", bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_700, width=600, height=50)
        self.copy_button = ft.IconButton(icon=ft.Icons.COPY, icon_color=ft.Colors.SECONDARY, tooltip="Copiar")
        self.theme_button = ft.IconButton(icon=ft.Icons.DARK_MODE, icon_color=ft.Colors.BLUE_400, on_click=self.toogle_theme)

    def get_password_length(self) -> int:
        return int(self.length_slider.value)

    def want_uppercase(self) -> bool:
        return self.uppercase_switch.value

    def want_numbers(self) -> bool:
        return self.numbers_switch.value

    def want_symbols(self) -> bool:
        return self.symbols_switch.value

    def show_password(self, password: str, entropy: float) -> None:
        self.password_output.value = password
        self.show_strength(entropy)
        self.page.update()

    def show_strength(self, entropy: float) -> None:
        if entropy < 28:
            label, color = "Muy débil", ft.Colors.RED_400
        elif entropy < 60:
            label, color = "Débil", ft.Colors.ORANGE_400
        elif entropy < 80:
            label, color = "Media", ft.Colors.AMBER_400
        elif entropy < 128:
            label, color = "Alta", ft.Colors.LIGHT_BLUE_400
        else:
            label, color = "Muy alta", ft.Colors.GREEN_400

        self.strength_bar.value = min(entropy / 128, 1)
        self.strength_bar.color = color
        self.strength_text.value = f"Seguridad: {label} ({entropy:.1f} bits)"
        self.strength_text.color = color

    def show_message(self, message: str) -> None:
        self.page.show_dialog(ft.SnackBar(ft.Text(message)))

    async def copy_to_clipboard(self):
                text = self.password_output.value
                await ft.Clipboard().set(text)
                self.show_message("Copiado al portapapeles")

    def show_error(self, message: str) -> None:
        self.password_output.value = ""
        self.length_slider.error_text = message
        self.page.update()

    def toogle_theme(self):
        self.theme_button.icon = ft.Icons.DARK_MODE if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.Icons.LIGHT_MODE
        self.page.theme_mode = ft.ThemeMode.DARK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        self.page.update()

    def build_ui(self):
        headerRow = ft.Container(
                        content = ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.LOCK_OUTLINE, color=ft.Colors.BLUE_400, size=24),
                            ft.Text("Generador de Contraseñas", size=24, weight=ft.FontWeight.BOLD, expand=True),
                            self.theme_button,
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        ),
                        padding=ft.Padding(left=0, top=0, right=0, bottom=20),
                    )

        passwordRow = ft.Card(
                        content=ft.Column([
                                ft.Text("CONTRASEÑA GENERADA", size=11, weight=ft.FontWeight.BOLD, color=ft.Colors.SECONDARY),
                                ft.Row([
                                    self.password_output,
                                    self.copy_button
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=10),
                                ft.Divider(height=20),
                                ft.Row([self.strength_bar, self.strength_text]),
                            ],
                            margin=20),
                        bgcolor=ft.Colors.ON_SECONDARY,
                    )

        generateRow = ft.Container(
                        content=self.generate_button,
                        padding=ft.Padding(left=0, top=10, right=0, bottom=10),
                    )

        lengthRow = ft.Card(
            content=ft.Column([
                ft.Row(
                    controls=[
                        ft.Text("LONGITUD DE LA CONTRASEÑA", size=11, weight=ft.FontWeight.BOLD, color=ft.Colors.SECONDARY, expand=True),
                        self.txt_length_number
                    ],
                    spacing=10
                ),
                self.length_slider,
                ft.Row(
                    controls=[
                        ft.Text("MIN: 8", size=11, weight=ft.FontWeight.BOLD, color=ft.Colors.SECONDARY, expand=True),
                        ft.Text("MAX: 32", size=11, weight=ft.FontWeight.BOLD, color=ft.Colors.SECONDARY)
                    ],
                    spacing=10
                ),
            ],
            margin=20),
            bgcolor=ft.Colors.ON_SECONDARY,
        )

        self.page.add(
            ft.SafeArea(
                ft.Column(
                    controls=[headerRow, passwordRow, generateRow, lengthRow],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        )
