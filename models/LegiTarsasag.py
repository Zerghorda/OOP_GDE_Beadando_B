from models.JegyFoglalas import JegyFoglalas

class LegiTarsasag:
    def __init__(self, nev):
        self._nev = nev
        self._jaratok = []
        self._foglalasok = []

    def get_nev(self):
        return self._nev

    def jarat_hozzaadas(self, jarat):
        self._jaratok.append(jarat)

    def foglalas(self, nev, jaratszam):
        for jarat in self._jaratok:
            if jarat.get_jaratszam() == jaratszam:
                uj = JegyFoglalas(nev, jarat)
                self._foglalasok.append(uj)
                return jarat.get_jegyar()
        raise Exception("Nincs ilyen járat!")

    def lemondas(self, nev, jaratszam):
        for f in self._foglalasok:
            if f.get_nev() == nev and f.get_jarat().get_jaratszam() == jaratszam:
                self._foglalasok.remove(f)
                return True
        raise Exception("Foglalás nem található!")

    def listaz(self):
        return [f.get_info() for f in self._foglalasok]