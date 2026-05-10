"""Ejemplo de composición donde una computadora contiene otras piezas."""

class Processor:
    """Clase que representa un procesador."""

    def __init__(self, model: str):
        self.model = model


class Memory:
    """Clase que representa memoria RAM."""

    def __init__(self, size: str):
        self.size = size


class Computer:
    """Clase que explica composición: una computadora tiene procesador y memoria."""

    def __init__(self, processor_model: str, memory_size: str):
        self.processor = Processor(processor_model)
        self.memory = Memory(memory_size)

    def show_specs(self) -> list[str]:
        return [
            f"Procesador: {self.processor.model}",
            f"Memoria RAM: {self.memory.size}",
        ]


if __name__ == "__main__":
    computer = Computer("Intel i7", "16 GB")
    for line in computer.show_specs():
        print(line)
