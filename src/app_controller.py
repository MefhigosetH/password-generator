from app_model import AppModel
from app_view import AppView


class AppController:
    def __init__(self, model: AppModel, view: AppView) -> None:
        self.model = model
        self.view = view
        self.view.generate_button.on_click = self.handle_generate
        self.view.length_slider.on_change = self.handle_generate
        self.view.uppercase_switch.on_change = self.handle_generate
        self.view.numbers_switch.on_change = self.handle_generate
        self.view.symbols_switch.on_change = self.handle_generate

    def handle_generate(self, _: object) -> None:
        try:
            length = self.view.get_password_length()
            password = self.model.generate_password(length,
                                                    self.view.get_include_uppercase(),
                                                    self.view.get_include_numbers(),
                                                    self.view.get_include_symbols())
        except ValueError as error:
            self.view.show_error(str(error))
            return

        self.view.show_password(password)