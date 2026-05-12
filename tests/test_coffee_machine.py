"""Modulo de pruebas: valida la secuencia de abstraccion en CoffeeMachine."""

from oop_python_fundamentos.abstraccion.coffee_machine import CoffeeMachine


def test_make_coffee_runs_internal_steps_in_order():
    machine = CoffeeMachine()

    output_lines = machine.make_coffee()

    assert output_lines == [
        "Calentando agua",
        "Moliendo café",
        "Sirviendo café",
        "Café listo",
    ]


def test_internal_abstraction_methods_are_not_public():
    machine = CoffeeMachine()

    assert not hasattr(machine, "heat_water")
    assert not hasattr(machine, "grind_coffee")
    assert not hasattr(machine, "serve_coffee")
