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

    avg_penguasaan_materi = round(sum_penguasan_materi/total_feedback, 2)
    avg_sistematika_penyajian = round(sum_sistematika_penyajian/total_feedback, 2)
    avg_metode_penyajian = round(sum_metode_penyajian/total_feedback, 2)
    avg_pengaturan_waktu = round(sum_pengaturan_waktu/total_feedback, 2)
    avg_penggunaan_alat_bantu = round(sum_penggunaan_alat_bantu/total_feedback, 2)

    total_avg = avg_penguasaan_materi + avg_sistematika_penyajian + avg_metode_penyajian + avg_pengaturan_waktu + avg_penggunaan_alat_bantu
    overall = round(total_avg/5, 2)

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
            overall,
            positive_comment,
            improvement_comment
        )

    return report
