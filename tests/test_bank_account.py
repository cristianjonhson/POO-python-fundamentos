from oop_python_fundamentals.encapsulation.bank_account import BankAccount


def test_deposit_increases_balance():
    account = BankAccount("Cristian", 1000)

    account.deposit(500)

    assert account.get_balance() == 1500


def test_withdraw_decreases_balance():
    account = BankAccount("Cristian", 1000)

    account.withdraw(300)

    assert account.get_balance() == 700


def test_withdraw_more_than_balance_does_not_change_balance():
    account = BankAccount("Cristian", 1000)

    account.withdraw(2000)

    assert account.get_balance() == 1000
