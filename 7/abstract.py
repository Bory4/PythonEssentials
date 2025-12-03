from abc import ABC, abstractmethod 

class RegulaDetekcji(ABC):
    
    @abstractmethod
    def analizuj(self, pakiet):
        pass

    @abstractmethod
    def pobierz_nazwe(self):
        pass

    def loguj_wykrycie(self, pakiet):
        print(f"{pakiet}")

class RegulaSQLInjection(RegulaDetekcji):
    def analizuj(self, pakiet):
        skluczowe = ["SELECT", "DROP", "UNION"]
        for i in skluczowe:
            if i in pakiet:
                return True
        return False
    
    def pobierz_nazwe(self):
        return __class__.__name__
    
class RegulaXSS(RegulaDetekcji):
    def analizuj(self, pakiet):
        skluczowe = ["<script", "<script>"]
        for i in skluczowe:
            if i in pakiet:
                return True
        return False
    
    def pobierz_nazwe(self):
        return __class__.__name__

if __name__ == "__main__":
    pakiety = ["Zły sqli SELECT * FROM DATABASE", "<script>alert(1)</script>", "GET https://guthib.com"]   
    
    sprawdzaczsqli = RegulaSQLInjection()
    sprawdzaczxss = RegulaXSS()

    for pakiet in pakiety:
        print(f"{sprawdzaczsqli.pobierz_nazwe()} -> {sprawdzaczsqli.analizuj(pakiet)}")
        print(f"{sprawdzaczxss.pobierz_nazwe()} -> {sprawdzaczxss.analizuj(pakiet)}")
    