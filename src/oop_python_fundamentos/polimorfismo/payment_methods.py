"""Colección de métodos de pago para ejemplificar comportamiento polimórfico."""

class PaymentMethod:
    """Clase base para explicar polimorfismo."""

    def __init__(self, amount: float):
        self.amount = amount

    def pay(self) -> None:
        print("Procesando pago genérico")


class CreditCardPayment(PaymentMethod):
    def pay(self) -> None:
        print(f"Pago de ${self.amount} realizado con tarjeta de crédito")


class PayPalPayment(PaymentMethod):
    def pay(self) -> None:
        print(f"Pago de ${self.amount} realizado con PayPal")


class BankTransferPayment(PaymentMethod):
    def pay(self) -> None:
        print(f"Pago de ${self.amount} realizado por transferencia bancaria")


if __name__ == "__main__":
    payments = [
        CreditCardPayment(10000),
        PayPalPayment(15000),
        BankTransferPayment(20000),
    ]

    for payment in payments:
        payment.pay()
