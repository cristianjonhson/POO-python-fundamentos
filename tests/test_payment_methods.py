"""Modulo de pruebas: valida el comportamiento polimorfico de los pagos."""

from oop_python_fundamentos.polimorfismo.payment_methods import (
    CreditCardPayment,
    PayPalPayment,
    BankTransferPayment,
)


def test_payment_methods_share_common_interface():
    payments = [
        CreditCardPayment(10000),
        PayPalPayment(15000),
        BankTransferPayment(20000),
    ]

    assert all(hasattr(payment, "pay") for payment in payments)


def test_polymorphism_executes_specific_payment_behavior():
    payments = [
        CreditCardPayment(10000),
        PayPalPayment(15000),
        BankTransferPayment(20000),
    ]

    output_lines = [payment.pay() for payment in payments]

    assert output_lines == [
        "Pago de $10000 realizado con tarjeta de crédito",
        "Pago de $15000 realizado con PayPal",
        "Pago de $20000 realizado por transferencia bancaria",
    ]
