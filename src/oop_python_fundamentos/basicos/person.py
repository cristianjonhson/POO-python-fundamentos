"""Modulo educativo: modelo sencillo de persona para practicar objetos."""

class Person:
    """Clase simple para representar una persona."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_info(self) -> None:
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")


if __name__ == "__main__":
    person = Person("Ana", 25)
    person.show_info()
