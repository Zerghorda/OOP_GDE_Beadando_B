from models.Jarat import Jarat

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar * 0.8)
        self._ido = 1

    def get_tipus(self):
        return "Belföldi"

    def get_ido(self):
        return self._ido