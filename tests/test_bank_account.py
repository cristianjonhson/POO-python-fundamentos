"""Modulo de pruebas: valida operaciones y reglas de BankAccount."""

import pytest

from oop_python_fundamentos.encapsulamiento.bank_account import BankAccount


def test_deposit_increases_balance():
    account = BankAccount("Cristian", 1000)

    result = account.deposit(500)

    assert result == "Depósito realizado: 500"
    assert account.get_balance() == 1500


def test_withdraw_decreases_balance():
    account = BankAccount("Cristian", 1000)

    result = account.withdraw(300)

    assert result == "Retiro realizado: 300"
    assert account.get_balance() == 700


def test_withdraw_more_than_balance_does_not_change_balance():
    account = BankAccount("Cristian", 1000)

    result = account.withdraw(2000)

    assert result == "Saldo insuficiente"
    assert account.get_balance() == 1000


def test_negative_initial_balance_raises_value_error():
    with pytest.raises(ValueError, match="saldo inicial"):
        BankAccount("Cristian", -1)


def test_non_positive_deposit_does_not_change_balance():
    account = BankAccount("Cristian", 1000)

    result_zero = account.deposit(0)
    result_negative = account.deposit(-50)

    assert result_zero == "El depósito debe ser mayor a cero"
    assert result_negative == "El depósito debe ser mayor a cero"
    assert account.get_balance() == 1000


def test_non_positive_withdraw_does_not_change_balance():
    account = BankAccount("Cristian", 1000)

    result_zero = account.withdraw(0)
    result_negative = account.withdraw(-50)

    assert result_zero == "El retiro debe ser mayor a cero"
    assert result_negative == "El retiro debe ser mayor a cero"
    assert account.get_balance() == 1000
