import pytest

from unittest.mock import MagicMock
from euphemos.feedback.repository.gsheet import GsheetRepository

spreadsheet_id = 'some_complex_id'
range_name = 'Form Responses!A2:L'


@pytest.fixture
def repository():
    return GsheetRepository(service=MagicMock(), spreadsheet_id=spreadsheet_id, range_name=range_name)


def test_fetchall_none_result(repository):
    values = []
    result = MagicMock()
    result.get.return_value = values

    config = {'spreadsheets.return_value.values.return_value.get.return_value.execute.return_value': result}
    repository.service.configure_mock(**config)

    assert len(repository.fetchall()) == 0


def test_fetchall(repository):
    values = [
        ['10/27/2015 21:02:52', 'Sergey Brin', 'Rasuna 1', 'group 2', 4, 4, 4, 5, 5, 5, 'Ok lah', 'Improve donk'],
        ['10/27/2015 21:02:52', 'Larry Page', 'Rasuna 3', 'group 2', 4, 4, 4, 5, 5, 5, 'Ok lah', 'Improve donk'],
        ['10/27/2015 21:02:52', 'Mark', 'Rasuna 5', 'group 2', 4, 4, 4, 5, 5, 5, 'Ok lah', 'Improve donk']
    ]
    result = MagicMock()
    result.get.return_value = values

    config = {'spreadsheets.return_value.values.return_value.get.return_value.execute.return_value': result}
    repository.service.configure_mock(**config)

    assert len(repository.fetchall()) == 3
