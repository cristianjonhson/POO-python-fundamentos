"""Modulo educativo: ejecuta la demostracion principal de conceptos POO."""

from src.oop_python_fundamentos.basicos.car import Car
from src.oop_python_fundamentos.basicos.person import Person
from src.oop_python_fundamentos.encapsulamiento.bank_account import BankAccount
from src.oop_python_fundamentos.herencia.students import Student
from src.oop_python_fundamentos.polimorfismo.payment_methods import CreditCardPayment, PayPalPayment
from src.oop_python_fundamentos.abstraccion.coffee_machine import CoffeeMachine
from src.oop_python_fundamentos.composicion.computer import Computer
from src.oop_python_fundamentos.metodos_especiales.product import Product


def main():
    print("=== Fundamentos de POO en Python ===")

    print("\n1. Clase, objeto, atributo y método")
    car = Car("Ford", "Fiesta")
    car.show()

    print("\n2. Clase Person")
    person = Person("Ana", 25)
    person.show_info()

    print("\n3. Encapsulamiento")
    account = BankAccount("Cristian", 1000)
    print(account.deposit(500))
    print(account.withdraw(300))
    print(f"Saldo actual: {account.get_balance()}")

    print("\n4. Herencia")
    student = Student("Ana", "Python")
    for line in student.show_info():
        print(line)

    print("\n5. Polimorfismo")
    payments = [
        CreditCardPayment(15000),
        PayPalPayment(20000),
    ]

    for payment in payments:
        print(payment.pay())

    print("\n6. Abstracción")
    machine = CoffeeMachine()
    for step in machine.make_coffee():
        print(step)

    print("\n7. Composición")
    computer = Computer("Intel i7", "16 GB")
    for line in computer.show_specs():
        print(line)

    print("\n8. Métodos especiales")
    product = Product("Curso de Python", 25000)
    print(product)


if __name__ == "__main__":
    main()
