"""Producto que usa propiedades para validar el acceso a su precio."""

class ProductWithProperty:
    """Clase para explicar el uso de @property y setters."""

    def __init__(self, name: str, price: float):
        self.name = name
        self.__price = 0
        self.price = price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("El precio debe ser mayor a cero")

        self.__price = value


if __name__ == "__main__":
    product = ProductWithProperty("Curso de Python", 25000)
    print(product.price)
    product.price = 30000
    print(product.price)
