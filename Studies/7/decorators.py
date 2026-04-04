import re

class Uzytkownik:
    licznikUzytkownikow = 0
    role = ["admin","analyst","viewer"]
    def __init__(self, login, rola):
        self.licznikUzytkownikow += 1
        self.login = login
        self.rola = rola

    @staticmethod
    def waliduj_login(login):

        if (len(login) > 2 and len(login) < 21) and re.match("[a-zA-Z0-9_]*"):
            return True
        else:
            return False
            
    @classmethod
    def pobierz_statystyki(cls):
        return {licznikUzytkownikow:role}
    @classmethod
    def utworz_admina(cls, login):
        def __init__(self, login, rola):
        self.login = login
        self.rola = "admin"