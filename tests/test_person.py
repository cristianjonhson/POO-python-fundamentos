from oop_python_fundamentos.basicos.person import Person


def test_person_attributes():
    person = Person("Ana", 25)

    assert person.name == "Ana"
    assert person.age == 25
