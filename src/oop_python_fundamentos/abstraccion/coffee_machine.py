"""Modulo educativo: ejemplo de abstraccion con una cafetera."""

class CoffeeMachine:
    """Clase para explicar abstracción ocultando pasos internos."""

    def make_coffee(self) -> list[str]:
        return [
            self.__heat_water(),
            self.__grind_coffee(),
            self.__serve_coffee(),
            "Café listo",
        ]

    def __heat_water(self) -> str:
        return "Calentando agua"

    def __grind_coffee(self) -> str:
        return "Moliendo café"

    def __serve_coffee(self) -> str:
        return "Sirviendo café"


if __name__ == "__main__":
    machine = CoffeeMachine()
    for step in machine.make_coffee():
        print(step)
