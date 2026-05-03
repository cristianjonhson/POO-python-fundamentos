from oop_python_fundamentos.composition.computer import Computer, Processor, Memory


def test_computer_builds_composed_objects():
    computer = Computer("Intel i7", "16 GB")

    assert isinstance(computer.processor, Processor)
    assert isinstance(computer.memory, Memory)
    assert computer.processor.model == "Intel i7"
    assert computer.memory.size == "16 GB"


def test_computer_show_specs_prints_expected_output(capsys):
    computer = Computer("Intel i7", "16 GB")

    computer.show_specs()

    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()

    assert output_lines == [
        "Procesador: Intel i7",
        "Memoria RAM: 16 GB",
    ]
