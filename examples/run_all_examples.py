from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from oop_python_fundamentos.basicos.car import Car
from oop_python_fundamentos.basicos.person import Person
from oop_python_fundamentos.encapsulamiento.bank_account import BankAccount
from oop_python_fundamentos.herencia.animals import Dog, Cat
from oop_python_fundamentos.polimorfismo.payment_methods import (
    CreditCardPayment,
    PayPalPayment,
    BankTransferPayment,
)
from oop_python_fundamentos.abstraccion.coffee_machine import CoffeeMachine
from oop_python_fundamentos.composicion.computer import Computer
from oop_python_fundamentos.metodos_especiales.product import Product


def run_all_examples():
    print("Ejecutando todos los ejemplos de POO en Python")

    car = Car("Ford", "Fiesta")
    car.show()

    person = Person("Ana", 25)
    person.show_info()

    account = BankAccount("Cristian", 1000)
    account.deposit(100)
    print(f"Saldo actual: {account.get_balance()}")

    animals = [Dog("Firulais"), Cat("Michi")]
    for animal in animals:
        animal.sound()

    payments = [
        CreditCardPayment(10000),
        PayPalPayment(15000),
        BankTransferPayment(20000),
    ]

    for payment in payments:
        payment.pay()

    machine = CoffeeMachine()
    machine.make_coffee()

    computer = Computer("Intel i7", "16 GB")
    computer.show_specs()

    product = Product("Curso de Python", 25000)
    print(product)


if __name__ == "__main__":
    run_all_examples()
