import random
import string
import logging

class AppModel:
    _CHARACTERS = string.ascii_lowercase

    def __init__(self) -> None:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger("AppModel")

    def generate_password(self, length: int, use_uppercase: bool, use_digits: bool, use_punctuation: bool) -> str:
        if not 1 <= length <= 128:
            raise ValueError("La longitud debe estar entre 1 y 128 caracteres.")

        if use_uppercase:
            self._CHARACTERS += string.ascii_uppercase
        if use_digits:
            self._CHARACTERS += string.digits
        if use_punctuation:
            self._CHARACTERS += string.punctuation

        if not self._CHARACTERS:
            raise ValueError("Debe seleccionar al menos un tipo de carácter.")

        return "".join(random.choice(self._CHARACTERS) for _ in range(length))
