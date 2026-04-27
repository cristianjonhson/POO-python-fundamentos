from oop_python_fundamentals.basics.car import Car


def test_car_attributes():
    car = Car("Ford", "Fiesta")

    assert car.brand == "Ford"
    assert car.model == "Fiesta"
