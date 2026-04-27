from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from oop_python_fundamentals.basics.car import Car
from oop_python_fundamentals.basics.person import Person
from oop_python_fundamentals.encapsulation.bank_account import BankAccount
from oop_python_fundamentals.inheritance.animals import Dog, Cat
from oop_python_fundamentals.polymorphism.payment_methods import CreditCardPayment, PayPalPayment
from oop_python_fundamentals.abstraction.coffee_machine import CoffeeMachine
from oop_python_fundamentals.composition.computer import Computer
from oop_python_fundamentals.dunder_methods.product import Product


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
    account.deposit(500)
    account.withdraw(300)
    print(f"Saldo actual: {account.get_balance()}")

    print("\n4. Herencia")
    dog = Dog("Firulais")
    cat = Cat("Michi")
    dog.sound()
    cat.sound()

    print("\n5. Polimorfismo")
    payments = [
        CreditCardPayment(15000),
        PayPalPayment(20000),
    ]

    for payment in payments:
        payment.pay()

    print("\n6. Abstracción")
    machine = CoffeeMachine()
    machine.make_coffee()

    print("\n7. Composición")
    computer = Computer("Intel i7", "16 GB")
    computer.show_specs()

    print("\n8. Métodos especiales")
    product = Product("Curso de Python", 25000)
    print(product)


if __name__ == "__main__":
    main()
