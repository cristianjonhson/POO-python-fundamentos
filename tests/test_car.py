"""Modulo de pruebas: valida el comportamiento basico del modelo Car."""

from oop_python_fundamentos.basicos.car import Car


def test_car_attributes():
    car = Car("Ford", "Fiesta")

    assert car.brand == "Ford"
    assert car.model == "Fiesta"
