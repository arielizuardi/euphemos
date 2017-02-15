from euphemos.report.presenter_evaluation import PresenterEvaluationReport
from euphemos.container import container


def get_report(session, batch, year, presenter=None):
    """
    Get report for following session, batch, year
    Args:
        session(int): The session
        batch(int): The batch
        year (int): The year
        presenter(str): The presenter, could be empty

    Returns:
        euphemos.report.presenter_evaluation.PresenterEvaluationReport
    """
    feedback_presenters = container.feedback_presenter_repository.fetch(
        session=session,
        batch=batch,
        year=year,
        presenter=presenter
    )

    total_feedback = len(feedback_presenters)
    if total_feedback == 0:
        return None

    sum_penguasan_materi = 0
    sum_sistematika_penyajian = 0
    sum_metode_penyajian = 0
    sum_penggunaan_alat_bantu = 0
    sum_pengaturan_waktu = 0

    for feedback_presenter in feedback_presenters :
        sum_penguasan_materi += feedback_presenter.penguasaan_materi
        sum_sistematika_penyajian += feedback_presenter.sistematika_penyajian
        sum_metode_penyajian += feedback_presenter.metode_penyajian
        sum_pengaturan_waktu += feedback_presenter.pengaturan_waktu
        sum_penggunaan_alat_bantu += feedback_presenter.penggunaan_alat_bantu

    avg_penguasaan_materi = sum_penguasan_materi/total_feedback
    avg_sistematika_penyajian = sum_sistematika_penyajian/total_feedback
    avg_metode_penyajian = sum_metode_penyajian/total_feedback
    avg_pengaturan_waktu  = sum_pengaturan_waktu/total_feedback
    avg_penggunaan_alat_bantu = sum_penggunaan_alat_bantu/total_feedback

    presenter = ''
    positive_comment = ''
    improvement_comment = ''

    report = PresenterEvaluationReport(
            batch,
            year,
            session,
            presenter,
            avg_penguasaan_materi,
            avg_sistematika_penyajian,
            avg_metode_penyajian,
            avg_pengaturan_waktu,
            avg_penggunaan_alat_bantu,
            positive_comment,
            improvement_comment
        )

    return report
