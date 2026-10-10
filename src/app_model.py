import secrets
import string


class AppModel:
    _CHARACTERS = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self, length: int) -> str:
        if not 1 <= length <= 128:
            raise ValueError("La longitud debe estar entre 1 y 128 caracteres.")

        return "".join(secrets.choice(self._CHARACTERS) for _ in range(length))