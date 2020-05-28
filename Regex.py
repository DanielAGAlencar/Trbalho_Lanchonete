import re


class Regex:

    def valida_id(id):
        if not re.fullmatch(r"\d{0,9}", id):
            print("Id Invalido")
            return True
        else:
            return False

    def valida_tel(tel):
        if not re.fullmatch(r"(\(?\d{2}\)?\s?\-?\s?)?(\d{4,5}\-?\d{4})", tel):
            print("Telefone invalido!")
            return True
        else:
            return False

    def valida_valores(valor):
        if not re.fullmatch(r"(\d{1,3}\.)?(\d{1,3}\.)?(\d{1,3}\.)?(\d{1,3}\,)(\d{2})", valor):
            print("Valor Invalido!")
            return True
        else:
            return False