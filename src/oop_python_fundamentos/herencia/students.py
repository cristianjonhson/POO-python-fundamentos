"""Modulo educativo: ejemplo de herencia entre persona y estudiante."""

class Person:
    """Clase padre."""

    def __init__(self, name: str):
        self.name = name


class Student(Person):
    """Clase hija que usa super() para reutilizar el constructor padre."""

    def __init__(self, name: str, course: str):
        super().__init__(name)
        self.course = course

    def show_info(self) -> list[str]:
        return [
            f"Estudiante: {self.name}",
            f"Curso: {self.course}",
        ]


if __name__ == "__main__":
    student = Student("Ana", "Python")
    for line in student.show_info():
        print(line)
