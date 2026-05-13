"""Modulo de pruebas: valida herencia y salida del modelo Student."""

from oop_python_fundamentos.herencia.students import Person, Student


def test_student_inherits_person_and_sets_attributes():
    student = Student("Ana", "Python")

    assert isinstance(student, Person)
    assert student.name == "Ana"
    assert student.course == "Python"


def test_student_show_info_returns_expected_lines():
    student = Student("Ana", "Python")

    output_lines = student.show_info()

    assert output_lines == [
        "Estudiante: Ana",
        "Curso: Python",
    ]
