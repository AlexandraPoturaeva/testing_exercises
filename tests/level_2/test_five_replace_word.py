import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    'text, expected',
    [
        ('welcome to the jungle', 'welcome to the forest'),
        (
            'welcome to the jungle we got your disease in the jungle',
            'welcome to the forest we got your disease in the forest'
        ),
    ]
)
def test__replace_word__replace_one_or_more_word(text, replace_from, replace_to, expected):
    assert replace_word(text=text, replace_from=replace_from, replace_to=replace_to) == expected


def test__replace_word__doesnt_work_with_punctuation(replace_from, replace_to):
    text = 'welcome to the jungle. we got your disease in the jungle'
    actual_result = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)
    assert actual_result == 'welcome to the jungle. we got your disease in the forest'


def test__replace_word__independent_from_letter_case(replace_from, replace_to):
    text = 'Welcome to the JunGle we got your disease in the jungle'
    actual_result = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)
    assert actual_result == 'Welcome to the forest we got your disease in the forest'


def test__replace_word__doesnt_replace_gaps():
    text = 'welcome to the jungle'
    replace_from = ' '
    replace_to = '_'

    actual_result = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)

    assert actual_result == 'welcome to the jungle'
