import pytest

from functions.level_2.three_first import first


def test__first__with_items():
    assert first(items=[1, 2, 3]) == 1


def test__first__without_items_and_default():
    with pytest.raises(AttributeError):
        first(items=[])


@pytest.mark.parametrize(
    'default,expected',
    [
        (-10, -10),
        (None, None),
        ('helloworld', 'helloworld'),
    ]
)
def test__first__without_items_and_with_default(default, expected):
    items = []
    assert first(items=items, default=default) == expected
