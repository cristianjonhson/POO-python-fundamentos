"""Modulo educativo: modelo simple de auto para introducir atributos y metodos."""

class Car:
    """Clase básica para explicar clase, objeto, atributos, métodos, __init__ y self."""

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def show(self) -> None:
        print(f"Auto: {self.brand} {self.model}")


if __name__ == "__main__":
    car = Car("Ford", "Fiesta")
    car.show()
