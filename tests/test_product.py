from oop_python_fundamentos.metodos_especiales.product import Product


def test_product_equality():
    product_1 = Product("Curso de Python", 25000)
    product_2 = Product("Curso de Python", 25000)

    assert product_1 == product_2


def test_product_str():
    product = Product("Curso de Python", 25000)

    assert str(product) == "Producto: Curso de Python - Precio: $25000"
