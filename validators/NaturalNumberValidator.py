from prompt_toolkit.validation import Validator, ValidationError
import regex

class NaturalNumberValidator(Validator):
    def validate(self, document):
        isNumber = regex.match('^\d+$', document.text)
        if not isNumber:
            raise ValidationError(
                message='Por favor ingrese un numero valido(entero positivo)',
                cursor_position=len(document.text)) # Move cursor to end