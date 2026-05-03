import pytest

from oop_python_fundamentos.encapsulation.product_with_property import ProductWithProperty


def test_product_with_property_initializes_price():
    product = ProductWithProperty("Curso de Python", 25000)

    assert product.name == "Curso de Python"
    assert product.price == 25000


def test_product_with_property_setter_updates_price():
    product = ProductWithProperty("Curso de Python", 25000)

    product.price = 30000

    assert product.price == 30000


def test_product_with_property_rejects_non_positive_price_on_init():
    with pytest.raises(ValueError, match="precio debe ser mayor a cero"):
        ProductWithProperty("Curso de Python", 0)



def test_product_with_property_rejects_non_positive_price_on_setter():
    product = ProductWithProperty("Curso de Python", 25000)

    with pytest.raises(ValueError, match="precio debe ser mayor a cero"):
        product.price = -100
