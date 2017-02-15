from unittest.mock import patch, PropertyMock

from euphemos.container import container
from euphemos.report.presenter_evaluation.get import get_report


@patch('euphemos.container.Container.feedback_presenter_repository',
       new_callable=PropertyMock)
def test_get_non_existing_presenter_evaluation_report(_):

    container.feedback_presenter_repository.fetch.return_value = []
    found_evaluation_report = get_report(session=1, batch=1, year=1980, presenter=None)

    assert found_evaluation_report is None

    container.feedback_presenter_repository.fetch.assert_called_once_with(session=1, batch=1, year=1980, presenter=None)
