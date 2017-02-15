from unittest.mock import patch, PropertyMock

from euphemos.container import container
from euphemos.feedback.feedback_presenter import FeedbackPresenter
from euphemos.report.presenter_evaluation.get import get_report


@patch('euphemos.container.Container.feedback_presenter_repository',
       new_callable=PropertyMock)
def test_get_non_existing_presenter_evaluation_report(_):

    container.feedback_presenter_repository.fetch.return_value = []
    found_evaluation_report = get_report(session=1, batch=1, year=1980, presenter=None)

    assert found_evaluation_report is None

    container.feedback_presenter_repository.fetch.assert_called_once_with(session=1, batch=1, year=1980, presenter=None)


@patch('euphemos.container.Container.feedback_presenter_repository',
       new_callable=PropertyMock)
def test_get_presenter_evaluation_report(_):

    f1 = FeedbackPresenter(_id=1, batch=1, year=2016, session=5,
                           presenter='Juferson', participant='Arie', participant_date='Rasuna 1',
                           group='1 Arie Ardaya L', penguasaan_materi=5, sistematika_penyajian=4,
                           metode_penyajian=3, pengaturan_waktu=2, penggunaan_alat_bantu=5,
                           nilai_keseluruhan=4, created_at='2016-01-01 00:00:00')

    f2 = FeedbackPresenter(_id=1, batch=1, year=2016, session=5,
                           presenter='Juferson', participant='Mondang', participant_date='Rasuna 1',
                           group='1 Arie Ardaya L', penguasaan_materi=5, sistematika_penyajian=4,
                           metode_penyajian=3, pengaturan_waktu=2, penggunaan_alat_bantu=5,
                           nilai_keseluruhan=4, created_at='2016-01-01 00:00:00')

    f3 = FeedbackPresenter(_id=1, batch=1, year=2016, session=5,
                           presenter='Juferson', participant='Icha', participant_date='Rasuna 1',
                           group='1 Arie Ardaya L', penguasaan_materi=5, sistematika_penyajian=3,
                           metode_penyajian=3, pengaturan_waktu=2, penggunaan_alat_bantu=3,
                           nilai_keseluruhan=4, created_at='2016-01-01 00:00:00')

    container.feedback_presenter_repository.fetch.return_value = [f1, f2, f3]

    found_evaluation_report = get_report(session=1, batch=1, year=2016)

    assert found_evaluation_report is not None
    assert found_evaluation_report.avg_penguasaan_materi == 5
    assert found_evaluation_report.avg_sistematika_penyajian == 3.67
    assert found_evaluation_report.avg_metode_penyajian == 3
    assert found_evaluation_report.avg_pengaturan_waktu == 2
    assert found_evaluation_report.avg_penggunaan_alat_bantu == 4.33
    assert found_evaluation_report.overall == 3.6