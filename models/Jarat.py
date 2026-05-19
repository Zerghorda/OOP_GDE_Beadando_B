from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float):
        if jegyar <= 0:
            raise ValueError("A jegyárnak pozitívnak kell lennie!")

        self._jaratszam = jaratszam
        self._celallomas = celallomas
        self._jegyar = jegyar

    # Getterek
    def get_jaratszam(self) -> str:
        return self._jaratszam

    def get_celallomas(self) -> str:
        return self._celallomas

    def get_jegyar(self) -> float:
        return self._jegyar

    # Absztrakt metódus
    @abstractmethod
    def get_tipus(self) -> str:
        pass