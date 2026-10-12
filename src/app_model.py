import secrets
import string
import logging
import math

class AppModel:
    _CHARACTERS = ""

    def __init__(self) -> None:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger("AppModel")

    def generate_password(self, length: int, use_uppercase: bool, use_digits: bool, use_punctuation: bool) -> str:
        if not 1 <= length <= 128:
            raise ValueError("La longitud debe estar entre 1 y 128 caracteres.")

        self._CHARACTERS = string.ascii_lowercase

        if use_uppercase:
            self._CHARACTERS += string.ascii_uppercase
        if use_digits:
            self._CHARACTERS += string.digits
        if use_punctuation:
            self._CHARACTERS += string.punctuation

        if not self._CHARACTERS:
            raise ValueError("Debe seleccionar al menos un tipo de carácter.")

        return "".join(secrets.choice(self._CHARACTERS) for _ in range(length))

    def calcular_entropia(self, password: str) -> float:
        if not password:
            return 0
            
        # Definir el tamaño del pool de caracteres (R)
        tiene_minusculas = any(c.islower() for c in password)
        tiene_mayusculas = any(c.isupper() for c in password)
        tiene_numeros = any(c.isdigit() for c in password)
        tiene_especiales = any(not c.isalnum() for c in password)
        
        pool = 0
        if tiene_minusculas: pool += 26
        if tiene_mayusculas: pool += 26
        if tiene_numeros: pool += 10
        if tiene_especiales: pool += 33  # Caracteres especiales estándar ASCII
        
        longitud = len(password)
        
        # Calcular entropía: L * log2(R)
        return longitud * math.log2(pool)