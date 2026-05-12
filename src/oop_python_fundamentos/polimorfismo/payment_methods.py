"""Modulo educativo: metodos de pago para ejemplificar polimorfismo."""

class PaymentMethod:
    """Clase base para explicar polimorfismo."""

    def __init__(self, amount: float):
        self.amount = amount

    def pay(self) -> str:
        return "Procesando pago genérico"


class CreditCardPayment(PaymentMethod):
    def pay(self) -> str:
        return f"Pago de ${self.amount} realizado con tarjeta de crédito"


class PayPalPayment(PaymentMethod):
    def pay(self) -> str:
        return f"Pago de ${self.amount} realizado con PayPal"


class BankTransferPayment(PaymentMethod):
    def pay(self) -> str:
        return f"Pago de ${self.amount} realizado por transferencia bancaria"


if __name__ == "__main__":
    payments = [
        CreditCardPayment(10000),
        PayPalPayment(15000),
        BankTransferPayment(20000),
    ]

    for payment in payments:
        print(payment.pay())
