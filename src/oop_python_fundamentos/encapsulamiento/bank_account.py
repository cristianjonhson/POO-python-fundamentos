"""Cuenta bancaria simple para practicar estado privado y validaciones."""

class BankAccount:
    """Clase para explicar encapsulamiento usando un atributo privado."""

    def __init__(self, owner: str, initial_balance: float = 0):
        self.owner = owner
        if initial_balance < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        self.__balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("El depósito debe ser mayor a cero")
            return

        self.__balance += amount
        print(f"Depósito realizado: {amount}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("El retiro debe ser mayor a cero")
            return

        if amount > self.__balance:
            print("Saldo insuficiente")
            return

        self.__balance -= amount
        print(f"Retiro realizado: {amount}")

    def get_balance(self) -> float:
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Cristian", 1000)
    account.deposit(500)
    account.withdraw(300)
    print(account.get_balance())
