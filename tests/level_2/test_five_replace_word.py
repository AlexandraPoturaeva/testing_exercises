import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    'text, expected',
    [
        pytest.param(
            'welcome to the jungle',
            'welcome to the forest',
            id='replace_one_word',
        ),
        pytest.param(
            'welcome to the jungle we got your disease in the jungle',
            'welcome to the forest we got your disease in the forest',
            id='replace_two_words',
        ),
        pytest.param(
            'welcome to the jungle. we got your disease in the jungle',
            'welcome to the jungle. we got your disease in the forest',
            id='doesnt_work_with_punctuation'
        ),
        pytest.param(
            'Welcome to the JunGle we got your disease in the jungle',
            'Welcome to the forest we got your disease in the forest',
            id='independent_from_letter_case'
        ),
    ]
)
def test__replace_word(text, replace_from, replace_to, expected):
    assert replace_word(text=text, replace_from=replace_from, replace_to=replace_to) == expected


def test__replace_word__doesnt_replace_gaps():
    text = 'welcome to the jungle'
    replace_from = ' '
    replace_to = '_'

    actual_result = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)

    assert actual_result == 'welcome to the jungle'
