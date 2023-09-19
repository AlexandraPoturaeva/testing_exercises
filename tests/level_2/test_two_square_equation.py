from functions.level_2.two_square_equation import solve_square_equation
import math
import pytest


@pytest.mark.parametrize(
    'square_coefficient,linear_coefficient,const_coefficient',
    [
        (3, -4, 2),
        (0, 0, -6),
        (2, 0, 4),
    ]
)
def test__solve_square_equation__no_roots(square_coefficient, linear_coefficient, const_coefficient):
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == (None, None)


@pytest.mark.parametrize(
    'square_coefficient,linear_coefficient,const_coefficient,expected',
    [
        (0, -2, 8, (4, None)),
        (2, 0, -8, (-2, 2)),
    ]
)
def test__solve_square_equation__without_square_coefficient(square_coefficient, linear_coefficient, const_coefficient, expected):
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == expected


def test__solve_square_equation__two_roots():
    assert solve_square_equation(1, -4, -5) == (-1, 5)


def test__solve_square_equation__with_float_nums():
    square_coefficient = -8.6
    linear_coefficient = 8.4
    const_coefficient = 2.7

    discriminant = linear_coefficient ** 2 - 4 * square_coefficient * const_coefficient
    root_left = (-linear_coefficient - math.sqrt(discriminant)) / (2 * square_coefficient)
    root_right = (-linear_coefficient + math.sqrt(discriminant)) / (2 * square_coefficient)

    actual_result = solve_square_equation(
        linear_coefficient=linear_coefficient,
        square_coefficient=square_coefficient,
        const_coefficient=const_coefficient,
    )

    assert actual_result == (root_left, root_right)
