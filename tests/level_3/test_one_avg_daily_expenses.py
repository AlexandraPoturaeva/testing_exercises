from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
from datetime import datetime
from decimal import Decimal


def test__calculate_average_daily_expenses(create_expense):
    expenses_at_one_date = [
        create_expense(amount=amount)
        for amount in map(Decimal, ['110.5', '108.4'])
    ]

    expenses_at_another_date = [
        create_expense(
            amount=amount,
            spent_at=datetime.fromisoformat('2023-09-09'),
        )
        for amount in map(Decimal, ['210.5', '308.4'])
    ]

    all_expenses = expenses_at_one_date + expenses_at_another_date

    assert calculate_average_daily_expenses(all_expenses) == Decimal('368.9')
