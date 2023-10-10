from functions.level_3.four_fraud import find_fraud_expenses
from decimal import Decimal


def test__find_fraud_expenses(create_expense, create_random_bankcard):
    frauds = [create_expense(card=create_random_bankcard()) for _ in range(3)]
    not_frauds = [create_expense(amount=Decimal(5000.01), card=create_random_bankcard()) for _ in range(3)]

    assert find_fraud_expenses(history=frauds + not_frauds) == frauds


def test__find_fraud_expenses__no_frauds(create_expense, create_random_bankcard):
    expenses = [create_expense(amount=Decimal(5000.01), card=create_random_bankcard()) for _ in range(3)]
    assert not find_fraud_expenses(history=expenses)


def test__find_fraud_expenses__not_enough_frauds(create_expense, create_random_bankcard):
    frauds = [create_expense(card=create_random_bankcard()) for _ in range(2)]
    not_frauds = [create_expense(amount=Decimal(5000.01), card=create_random_bankcard()) for _ in range(3)]

    assert not find_fraud_expenses(history=frauds + not_frauds)
