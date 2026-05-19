from models.BelfoldiJarat import BelfoldiJarat
from models.NemzetkoziJarat import NemzetkoziJarat
from models.LegiTarsasag import LegiTarsasag
from models.FoglalasKezelo import FoglalasKezelo


def inicializalas():
    lt = LegiTarsasag("Air Python")

    j1 = BelfoldiJarat("B101", "Debrecen", 10000)
    j2 = BelfoldiJarat("B102", "Szeged", 12000)
    j3 = NemzetkoziJarat("N201", "London", 50000)

    lt.jarat_hozzaadas(j1)
    lt.jarat_hozzaadas(j2)
    lt.jarat_hozzaadas(j3)

    kezelo = FoglalasKezelo(lt)

    kezelo.jegy_foglalasa("Anna", "B101")
    kezelo.jegy_foglalasa("Béla", "B101")
    kezelo.jegy_foglalasa("Cecil", "B102")
    kezelo.jegy_foglalasa("Dani", "N201")
    kezelo.jegy_foglalasa("Emma", "N201")
    kezelo.jegy_foglalasa("Feri", "B102")

    return kezelo


def menu():
    kezelo = inicializalas()

    while True:
        print("\n1 - Foglalás")
        print("2 - Lemondás")
        print("3 - Listázás")
        print("0 - Kilépés")

        val = input("Választás: ")

        try:
            if val == "1":
                nev = input("Név: ")

                jaratok = kezelo._legitarsasag._jaratok
                print("\nElérhető járatok:")

                for i, j in enumerate(jaratok, start=1):
                    print(f"{i} - {j.get_jaratszam()} ({j.get_celallomas()}) - {j.get_jegyar()} Ft")

                valasztas = int(input("Válassz (szám): "))

                if valasztas < 1 or valasztas > len(jaratok):
                    print("Hibás választás!")
                    continue

                kivalasztott = jaratok[valasztas - 1]
                ar = kezelo.jegy_foglalasa(nev, kivalasztott.get_jaratszam())

                print(f"Sikeres foglalás! Ár: {ar} Ft")

            elif val == "2":
                nev = input("Név: ")

                foglalasok = kezelo.foglalasok_listazasa()
                sajat = [f for f in foglalasok if nev in f]

                if not sajat:
                    print("Nincs ilyen nevű foglalás.")
                    continue

                print("\nFoglalásaid:")
                for i, f in enumerate(sajat, start=1):
                    print(f"{i} - {f}")

                valasztas = int(input("Melyiket törlöd?: "))

                if valasztas < 1 or valasztas > len(sajat):
                    print("Hibás választás!")
                    continue

                kivalasztott = sajat[valasztas - 1]
                jaratszam = kivalasztott.split(" - ")[1].split(" ")[0]

                kezelo.foglalas_lemondas(nev, jaratszam)
                print("Sikeres lemondás")

            elif val == "3":
                foglalasok = kezelo.foglalasok_listazasa()
                if not foglalasok:
                    print("Nincs foglalás.")
                else:
                    for f in foglalasok:
                        print(f)

            elif val == "0":
                break

        except Exception as e:
            print("Hiba:", e)


if __name__ == "__main__":
    menu()