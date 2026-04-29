from oop_python_fundamentals.inheritance.students import Person, Student


def test_student_inherits_person_and_sets_attributes():
    student = Student("Ana", "Python")

    assert isinstance(student, Person)
    assert student.name == "Ana"
    assert student.course == "Python"


def test_student_show_info_prints_expected_output(capsys):
    student = Student("Ana", "Python")

    student.show_info()

    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()

    assert output_lines == [
        "Estudiante: Ana",
        "Curso: Python",
    ]
