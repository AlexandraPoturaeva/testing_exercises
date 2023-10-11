from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
from datetime import datetime, timedelta
from decimal import Decimal
import pytest


@pytest.mark.parametrize(
    'first_date',
    [
        datetime.today(),
        datetime.fromisoformat('1023-10-09'),
        datetime.fromisoformat('3023-10-09'),
    ],
    ids=[
        'actual dates',
        'very old dates',
        'future dates',
    ],

)
def test__calculate_average_daily_expenses(create_expense, first_date):
    expenses_at_one_date = [
        create_expense(
            amount=amount,
            spent_at=first_date,
        )
        for amount in map(Decimal, ['110.5', '108.4'])
    ]

    expenses_at_another_date = [
        create_expense(
            amount=amount,
            spent_at=first_date - timedelta(days=1),
        )
        for amount in map(Decimal, ['210.5', '308.4'])
    ]

    all_expenses = expenses_at_one_date + expenses_at_another_date

    assert calculate_average_daily_expenses(all_expenses) == Decimal('368.9')


@pytest.mark.parametrize(
    'first_date,second_date,expected',
    [
        ('2023-09-09 00:01 +0400', '2023-09-10 00:01 +0400', '110.5'),
        ('2023-09-09 00:01 +0400', '2023-09-09 00:01 +0000', '221'),
        ('2023-09-09 00:01 +0400', '2023-09-08 00:01 +0000', '110.5'),
    ],
    ids=[
        'different dates and same timezones',
        'same dates and different timezones',
        'different dates and different timezones',
    ]
)
def test__calculate_average_daily_expenses__with_timezones(create_expense, first_date, second_date, expected):
    expenses = [
        create_expense(
            amount=Decimal('110.5'),
            spent_at=datetime.strptime(date, '%Y-%m-%d %H:%M %z'),
        )
        for date in [first_date, second_date]
    ]

    assert calculate_average_daily_expenses(expenses) == Decimal(expected)
