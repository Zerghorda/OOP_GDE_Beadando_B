from models.Jarat import Jarat

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar * 1.2)
        self._ido = 3  # hosszabb út (óra)

    def get_tipus(self):
        return "Nemzetközi"

    def get_ido(self):
        return self._ido