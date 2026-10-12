import flet as ft

class AppView:

    def __init__(self, page: ft.Page):
        """Inicializa la interfaz de usuario, los controles y su disposición."""
        self.page = page
        self.page.title = "Generador de Contraseñas"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.bgcolor = "#121214"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 20
        self.page.scroll = ft.ScrollMode.AUTO

        self.uppercase_switch = ft.Switch(value=False, active_color=ft.Colors.BLUE_400)
        self.numbers_switch = ft.Switch(value=False, active_color=ft.Colors.BLUE_400)
        self.symbols_switch = ft.Switch(value=False, active_color=ft.Colors.BLUE_400)

        self.password_output = ft.TextField(value="",
                                            border=ft.NoInputBorder(),
                                            text_style=ft.TextStyle(
                                                font_family="monospace", 
                                                size=32, 
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.WHITE
                                            ),
                                            read_only=True,
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
                                        padding=15
                                    ),
                                    width=360,
                                )
        self.refresh_button = ft.IconButton(
                                                icon=ft.Icons.REFRESH,
                                                icon_color=ft.Colors.BLUE_400,
                                                tooltip="Generar nueva",
                                            )
        self.copy_button = ft.IconButton(
                                            icon=ft.Icons.COPY,
                                            icon_color=ft.Colors.GREEN_400,
                                            tooltip="Copiar",
                                        )

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

    def build_ui(self):
        # Estructura principal centrada (ideal para móviles / escritorio)
        self.page.add(
            ft.SafeArea(
                ft.Container(
                    padding=20,
                    border_radius=20,
                    bgcolor="#18181b",
                    shadow=ft.BoxShadow(spread_radius=1, blur_radius=15, color=ft.Colors.BLACK_54),
                    content=ft.Column(
                        [
                            # Título
                            ft.Row(
                                [
                                    ft.Icon(ft.Icons.LOCK_OUTLINE, color=ft.Colors.BLUE_400, size=24),
                                    ft.Text("Generador de Contraseñas", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
                                ],
                                alignment=ft.MainAxisAlignment.START,
                            ),

                            ft.Divider(color=ft.Colors.GREY_800),
                            
                            # Caja de Contraseña Generada con Acciones Rápidas
                            ft.Row(
                                [
                                    self.password_output,
                                    self.refresh_button,
                                    self.copy_button,
                                ],
                            ),

                            # Medidor de fuerza
                            ft.Column([
                                ft.Row([self.strength_text], alignment=ft.MainAxisAlignment.END),
                                self.strength_bar
                            ], spacing=4),
                            
                            ft.Divider(color=ft.Colors.GREY_800),
                            
                            # Sección de Opciones
                            ft.Text("Opciones de Configuración", size=14, weight=ft.FontWeight.W_500, color=ft.Colors.GREY_400),
                            
                            ft.Container(
                                padding=10,
                                border_radius=12,
                                bgcolor="#202024",
                                content=ft.Column([
                                    ft.Row([
                                        ft.Row([ft.Icon(ft.Icons.TEXT_FIELDS, size=18, color=ft.Colors.GREY_400), ft.Text("Incluir mayúsculas", color=ft.Colors.WHITE)]),
                                        self.uppercase_switch
                                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                    
                                    ft.Row([
                                        ft.Row([ft.Icon(ft.Icons.SIXTY_FPS_OUTLINED, size=18, color=ft.Colors.GREY_400), ft.Text("Incluir números", color=ft.Colors.WHITE)]),
                                        self.numbers_switch
                                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                    
                                    ft.Row([
                                        ft.Row([ft.Icon(ft.Icons.TAG, size=18, color=ft.Colors.GREY_400), ft.Text("Incluir símbolos", color=ft.Colors.WHITE)]),
                                        self.symbols_switch
                                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                ])
                            ),

                            # Sección de Longitud
                            ft.Row([
                                ft.Text("Longitud de caracteres", size=14, weight=ft.FontWeight.W_500, color=ft.Colors.GREY_400),
                                self.txt_length_number
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            
                            self.length_slider,

                            ft.VerticalDivider(),

                            # Botón Principal de Acción
                            #self.generate_button
                        ],
                        #tight=True,
                        spacing=15
                    ),
                ),
            )
        )
