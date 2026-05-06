class Product:
    """Clase para explicar métodos especiales como __str__ y __eq__."""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Producto: {self.name} - Precio: ${self.price}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return False

        return self.name == other.name and self.price == other.price


if __name__ == "__main__":
    product_1 = Product("Curso de Python", 25000)
    product_2 = Product("Curso de Python", 25000)

    print(product_1)
    print(product_1 == product_2)
