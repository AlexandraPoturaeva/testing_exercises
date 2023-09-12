import datetime
import pytest
from decimal import Decimal
from functions.level_1.four_bank_parser import BankCard, Expense


@pytest.fixture
def today_time():
    date = datetime.date.today()
    hour, minute = 10, 15
    return datetime.datetime(
        date.year,
        date.month,
        date.day,
        hour,
        minute
    )


@pytest.fixture
def tomorrow_time(today_time):
    return today_time + datetime.timedelta(days=1)


@pytest.fixture
def expense():
    return Expense(
        amount=Decimal('56'),
        card=BankCard(
            last_digits='8664',
            owner='IVAN IVANOV',
        ),
        spent_in='Mos.Transport 41 MIRA',
        spent_at=datetime.datetime(2023, 4, 4, 18, 14),
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
    good_words = {'love', 'caring'}
    return good_words


@pytest.fixture
def bad_words():
    bad_words = {'dislike', 'slow', 'bugs', 'frustration'}
    return bad_words