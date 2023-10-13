from functions.level_4.one_brackets import delete_remove_brackets_quotes
import pytest


@pytest.mark.parametrize(
    'name,expected',
    [
        ('{"name"}', 'name'),
        ('("name")', '("name")'),
        ('name', 'name'),
        ('{', ''),
        ('{"na', ''),
        ('{"nam', 'n'),
        ('{name}', 'am'),
        ('{name', 'a'),
    ]
)
def test__delete_remove_brackets_quotes(name, expected):
    assert delete_remove_brackets_quotes(name=name) == expected


def test__delete_remove_brackets_quotes__empty_line():
    with pytest.raises(IndexError):
        delete_remove_brackets_quotes('')
