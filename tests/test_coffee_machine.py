"""Pruebas que verifican la secuencia de abstracción en CoffeeMachine."""

from oop_python_fundamentos.abstraccion.coffee_machine import CoffeeMachine


def test_make_coffee_runs_internal_steps_in_order(capsys):
    machine = CoffeeMachine()

    machine.make_coffee()

    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()

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
