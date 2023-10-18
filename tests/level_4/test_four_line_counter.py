from functions.level_4.four_lines_counter import count_lines_in
import pytest


@pytest.mark.parametrize(
    'lines,expected',
    [
        (['1\n', '#\n'], 1),
        (['#\n'], 0),
        (None, 0),
    ]
)
def test__count_lines_in(filepath, lines, expected):
    assert count_lines_in(filepath(lines=lines)) == expected


def test__count_lines_in__with_dir(dir_path):
    assert count_lines_in(dir_path) is None
