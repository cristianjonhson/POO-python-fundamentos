"""Modulo educativo: jerarquia de animales para mostrar herencia."""

class Animal:
    """Clase padre para explicar herencia."""

    def __init__(self, name: str):
        self.name = name

    def eat(self) -> None:
        print(f"{self.name} está comiendo")

    def sound(self) -> None:
        print("El animal emite un sonido")


class Dog(Animal):
    """Clase hija que hereda de Animal."""

    def sound(self) -> None:
        print(f"{self.name} dice: Guau")


class Cat(Animal):
    """Clase hija que hereda de Animal."""

    def sound(self) -> None:
        print(f"{self.name} dice: Miau")


if __name__ == "__main__":
    dog = Dog("Firulais")
    cat = Cat("Michi")

    dog.eat()
    dog.sound()

    cat.eat()
    cat.sound()
