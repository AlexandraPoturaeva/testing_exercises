import pytest
from unittest.mock import patch

from functions.level_4.five_extra_fields import fetch_app_config_field, fetch_extra_fields_configuration


@pytest.mark.parametrize(
    'field_name,expected',
    [
        (
                'extra_fields',

                "TRAP_HTTP_EXCEPTIONS: False\n"
                "DEBUG: True\n"
                "SESSION_REFRESH_EACH_REQUEST: False"
        ),
        ('testing', None)
    ]
)
def test__fetch_app_config_field(config_file_path, field_name, expected):
    assert fetch_app_config_field(
        config_file_path=config_file_path,
        field_name=field_name
    ) == expected


def test__fetch_extra_fields_configuration__with_test_file(config_file_path):
    assert fetch_extra_fields_configuration(config_file_path) == {
        'TRAP_HTTP_EXCEPTIONS': False,
        'DEBUG': True,
        'SESSION_REFRESH_EACH_REQUEST': False
    }


def test__fetch_extra_fields_configuration__non_existent_path():
    assert fetch_extra_fields_configuration(config_file_path='any_path') == {}


def test__fetch_extra_fields_configuration__with_mock():
    with patch('functions.level_4.five_extra_fields.fetch_app_config_field') as fetch_app_config_field_mock:
        fetch_app_config_field_mock.return_value = \
            "TRAP_HTTP_EXCEPTIONS: False\n" \
            "DEBUG: True\n" \
            "SESSION_REFRESH_EACH_REQUEST: False"

        assert fetch_extra_fields_configuration(config_file_path='any_path') == {
            'TRAP_HTTP_EXCEPTIONS': False,
            'DEBUG': True,
            'SESSION_REFRESH_EACH_REQUEST': False
        }


def test__fetch_extra_fields_configuration__check_mock_args_list():
    with patch('functions.level_4.five_extra_fields.fetch_app_config_field') as fetch_app_config_field_mock:
        fetch_extra_fields_configuration('any_path')
        assert fetch_app_config_field_mock.call_args_list == [(('any_path', 'extra_fields'),)]
