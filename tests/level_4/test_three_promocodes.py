from functions.level_4.three_promocodes import generate_promocode
from unittest.mock import patch
import pytest


@pytest.mark.parametrize(
    'promocode_len,expected',
    [
        (6, 'G'*6),
        (0, ''),
        (-6, ''),
     ]
)
def test__generate_promocode__with_arg(promocode_len, expected):
    with patch('string.ascii_uppercase', 'G'):
        assert generate_promocode(promocode_len=promocode_len) == expected


def test__generate_promocode__without_arg():
    with patch('string.ascii_uppercase', 'G'):
        assert generate_promocode() == 'G' * 8
