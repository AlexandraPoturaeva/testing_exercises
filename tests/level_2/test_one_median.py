from functions.level_2.one_median import get_median_value
import pytest


@pytest.mark.parametrize(
    'list_of_nums, expected',
    [
        ([-500, 3, 5], 5),
        ([7, 9, 11, 3, -85944], 3),
        ([9, 11, -87455, 15, 3, 5, 7], 3),
    ]
)
def test__get_median_value__odd_number_of_elements_in_a_list__3_or_more_nums(list_of_nums, expected):
    assert get_median_value(list_of_nums) == expected


@pytest.mark.parametrize(
    'list_of_nums, expected',
    [
        ([1, 1, 1, 1, 3, 5], 4),
        ([-10000, 0, -15, 0, 0, 10, -1, 0], 4),
        ([8, 10, 12, 1, 3, 5, 7, 14, 16, 18], 10),
    ]
)
def test__get_median_value__even_number_of_elements_in_a_list__6_or_more_nums(list_of_nums, expected):
    assert get_median_value(list_of_nums) == expected


@pytest.mark.parametrize(
    'list_of_nums',
    [
        [1, 3, 5, 7],
        [1, 3],
    ]
)
def test__get_median_value__even_number_of_elements_in_a_list__4_or_less_nums(list_of_nums):
    with pytest.raises(IndexError):
        get_median_value(list_of_nums)


def test__get_median_value__one_element_in_a_list_of_nums():
    with pytest.raises(IndexError):
        get_median_value([2])


def test__get_median_value__empty_list_of_nums():
    assert not get_median_value([])


def test__get_median_value__str_with_odd_num_of_syms():
    assert get_median_value('fghyg') == 'y'


def test__get_median_value__str_with_even_num_of_syms():
    with pytest.raises(TypeError):
        get_median_value('fghygf')
