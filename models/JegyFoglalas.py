class JegyFoglalas:
    def __init__(self, nev, jarat):
        self._nev = nev
        self._jarat = jarat

    def get_nev(self):
        return self._nev

    def get_jarat(self):
        return self._jarat

    def get_info(self):
        return f"{self._nev} - {self._jarat.get_jaratszam()} ({self._jarat.get_celallomas()})"