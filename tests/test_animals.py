from oop_python_fundamentos.inheritance.animals import Animal, Dog, Cat


def test_dog_and_cat_are_animals():
    dog = Dog("Firulais")
    cat = Cat("Michi")

    assert isinstance(dog, Animal)
    assert isinstance(cat, Animal)


def test_dog_and_cat_sound_override_base_behavior(capsys):
    dog = Dog("Firulais")
    cat = Cat("Michi")

    dog.sound()
    cat.sound()

    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()

    assert output_lines == [
        "Firulais dice: Guau",
        "Michi dice: Miau",
    ]


def test_animal_eat_uses_inherited_implementation(capsys):
    dog = Dog("Firulais")

    dog.eat()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Firulais está comiendo"
