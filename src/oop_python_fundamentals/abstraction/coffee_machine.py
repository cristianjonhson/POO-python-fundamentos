class CoffeeMachine:
    """Clase para explicar abstracción ocultando pasos internos."""

    def make_coffee(self) -> None:
        self.__heat_water()
        self.__grind_coffee()
        self.__serve_coffee()
        print("Café listo")

    def __heat_water(self) -> None:
        print("Calentando agua")

    def __grind_coffee(self) -> None:
        print("Moliento café")

    def __serve_coffee(self) -> None:
        print("Sirviendo café")


if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.make_coffee()
