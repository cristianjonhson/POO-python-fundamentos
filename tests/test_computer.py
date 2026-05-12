"""Modulo de pruebas: valida la composicion interna de Computer."""

from oop_python_fundamentos.composicion.computer import Computer, Processor, Memory


def test_computer_builds_composed_objects():
    computer = Computer("Intel i7", "16 GB")

    assert isinstance(computer.processor, Processor)
    assert isinstance(computer.memory, Memory)
    assert computer.processor.model == "Intel i7"
    assert computer.memory.size == "16 GB"


def test_computer_show_specs_returns_expected_output():
    computer = Computer("Intel i7", "16 GB")

    output_lines = computer.show_specs()

    assert output_lines == [
        "Procesador: Intel i7",
        "Memoria RAM: 16 GB",
    ]
