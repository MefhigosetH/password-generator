import logging

from app_model import AppModel
from app_view import AppView


class AppController:
    def __init__(self, model: AppModel, view: AppView) -> None:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger("AppController")
        
        self.model = model
        self.view = view

        self.view.generate_button.on_click = self.handle_generate
        self.view.refresh_button.on_click = self.handle_generate
        self.view.copy_button.on_click = self.view.copy_to_clipboard
        self.view.length_slider.on_change = self.handle_generate
        self.view.uppercase_switch.on_change = self.handle_generate
        self.view.numbers_switch.on_change = self.handle_generate
        self.view.symbols_switch.on_change = self.handle_generate

    def handle_generate(self, _: object) -> None:
        try:
            length = self.view.get_password_length()
            self.view.txt_length_number.value = str(length)
            password = self.model.generate_password(length,
                                                    self.view.want_uppercase(),
                                                    self.view.want_numbers(),
                                                    self.view.want_symbols())
        except ValueError as error:
            self.view.show_error(str(error))
            return

        self.view.show_password(password)
