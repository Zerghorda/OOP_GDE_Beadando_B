from models.JegyFoglalas import JegyFoglalas

class FoglalasKezelo:
    def __init__(self, legitarsasag):
        self._legitarsasag = legitarsasag

    def jegy_foglalasa(self, nev, jaratszam):
        return self._legitarsasag.foglalas(nev, jaratszam)

    def foglalas_lemondas(self, nev, jaratszam):
        return self._legitarsasag.lemondas(nev, jaratszam)

    def foglalasok_listazasa(self):
        return self._legitarsasag.listaz()