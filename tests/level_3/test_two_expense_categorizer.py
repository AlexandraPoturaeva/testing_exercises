from functions.level_3.two_expense_categorizer import guess_expense_category
from functions.level_3.models import ExpenseCategory
import pytest


@pytest.mark.parametrize(
    'spent_in,expected',
    [
        ('-julis,', ExpenseCategory.BAR_RESTAURANT),
        ('apple.com/bill.pdf', ExpenseCategory.ONLINE_SUBSCRIPTIONS),
        ('alfa-pharm\\', ExpenseCategory.MEDICINE_PHARMACY),
        ('some place', None),
    ]
)
def test__guess_expense_category(create_expense, spent_in, expected):
    expense = create_expense(spent_in=spent_in)
    assert guess_expense_category(expense) == expected
