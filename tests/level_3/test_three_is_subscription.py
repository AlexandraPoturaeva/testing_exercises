from functions.level_3.three_is_subscription import is_subscription
from datetime import datetime


def test__is_subscription__return_true(create_expense):
    history = [
        create_expense(spent_at=datetime.fromisoformat(f'2023-0{month}-09'))
        for month in range(7, 10)
    ]
    assert is_subscription(expense=create_expense(), history=history) is True


def test__is_subscription__less_than_3_same_expenses_in_history(create_expense):
    history = [
        create_expense(spent_at=datetime.fromisoformat(f'2023-0{month}-09'))
        for month in range(8, 10)
    ]
    assert is_subscription(expense=create_expense(), history=history) is False


def test__is_subscription__no_same_expenses_in_history(create_expense):
    history = [
        create_expense(
            spent_in='netflix',
            spent_at=datetime.fromisoformat(f'2023-0{month}-09'))
        for month in range(7, 10)
    ]
    assert is_subscription(expense=create_expense(), history=history) is False


def test__is_subscription__more_than_1_same_expense_a_month(create_expense):
    history = [
        create_expense(spent_at=datetime.fromisoformat(f'2023-10-0{day}'))
        for day in range(1, 3)
    ]
    assert is_subscription(expense=create_expense(), history=history) is False
