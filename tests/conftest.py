import datetime
import pytest
import string
from decimal import Decimal
from datetime import date, datetime, timedelta
import random
from functions.level_1.four_bank_parser import BankCard, Expense as ExpenseLevel1
from functions.level_3.models import Expense as ExpenseLevel3, Currency


@pytest.fixture
def today_time():
    today_date = date.today()
    hour, minute = 10, 15
    return datetime(
        today_date.year,
        today_date.month,
        today_date.day,
        hour,
        minute
    )


@pytest.fixture
def tomorrow_time(today_time):
    return today_time + timedelta(days=1)


@pytest.fixture
def expense():
    return ExpenseLevel1(
        amount=Decimal('56'),
        card=BankCard(
            last_digits='8664',
            owner='IVAN IVANOV',
        ),
        spent_in='Mos.Transport 41 MIRA',
        spent_at=datetime(2023, 4, 4, 18, 14),
    )


@pytest.fixture
def cards():
    return [
        BankCard(
            last_digits='8664',
            owner='IVAN IVANOV',
        ),
        BankCard(
            last_digits='8564',
            owner='IVAN GROZNYJ',
        ),
        BankCard(
            last_digits='4789',
            owner='MALYUTA SCURATOV',
        ),
    ]


@pytest.fixture
def good_words():
    return {'love', 'caring'}


@pytest.fixture
def bad_words():
    return {'dislike', 'slow', 'bugs', 'frustration'}


@pytest.fixture
def replace_from():
    replace_from = 'jungle'
    return replace_from


@pytest.fixture
def replace_to():
    replace_to = 'forest'
    return replace_to


@pytest.fixture
def create_random_bankcard():
    def create_random_bankcard_function():
        letters = string.ascii_lowercase
        return BankCard(
            last_digits=str(random.randint(1000, 9999)),
            owner=''.join(random.choice(letters) for _ in range(5)),
        )
    return create_random_bankcard_function


@pytest.fixture()
def create_expense():
    def create_expense_function(
            amount=Decimal(100.5),
            currency=Currency.RUB,
            card=BankCard(last_digits='8668', owner='Ivan Ivanov'),
            spent_in='somewhere',
            spent_at=datetime.fromisoformat('2023-10-09'),
            category=None,
    ):
        expense = ExpenseLevel3(
            amount=amount,
            currency=currency,
            card=card,
            spent_in=spent_in,
            spent_at=spent_at,
            category=category,
        )
        return expense

    return create_expense_function
