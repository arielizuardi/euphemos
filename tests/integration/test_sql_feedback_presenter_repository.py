import pytest
from sqlalchemy.engine import create_engine
from db import create_tables
from euphemos.feedback.repository.sql import SQLRepository
from euphemos.feedback.repository.sql import feedback_presenter_table
from euphemos.feedback.feedback_presenter import FeedbackPresenter
from datetime import datetime


@pytest.fixture
def repository():
    engine = create_engine("sqlite:///:memory:")
    _repository = SQLRepository(sql_engine=engine)

    create_tables(sql_engine=engine)
    return _repository


def seed(repository, feedback_presenter):
    conn = repository.sql_engine.contextual_connect()
    trx = conn.begin()
    try:
        conn.execute(feedback_presenter_table.insert(), feedback_presenter.to_dict())
        trx.commit()
    except:
        trx.rollback()
        raise
    finally:
        conn.close()


def test_fetch(repository):

    t = datetime.now()
    f1 = FeedbackPresenter(_id=1, batch=1, year=2016, session=5,
                           presenter='Juferson', participant='Arie', participant_date='Rasuna 1',
                           group='1 Arie Ardaya L', penguasaan_materi=5, sistematika_penyajian=4,
                           metode_penyajian=3, pengaturan_waktu=2, penggunaan_alat_bantu=5,
                           nilai_keseluruhan=4, created_at=t)

    f2 = FeedbackPresenter(_id=2, batch=1, year=2016, session=3,
                           presenter='Alvi', participant='Mondang', participant_date='Rasuna 1',
                           group='1 Arie Ardaya L', penguasaan_materi=5, sistematika_penyajian=4,
                           metode_penyajian=3, pengaturan_waktu=2, penggunaan_alat_bantu=5,
                           nilai_keseluruhan=4, created_at=t)

    f3 = FeedbackPresenter(_id=3, batch=1, year=2016, session=5,
                           presenter='Juferson', participant='Icha', participant_date='Rasuna 1',
                           group='1 Arie Ardaya L', penguasaan_materi=5, sistematika_penyajian=3,
                           metode_penyajian=3, pengaturan_waktu=2, penggunaan_alat_bantu=3,
                           nilai_keseluruhan=4, created_at=t)

    seed(repository, f1)
    seed(repository, f2)
    seed(repository, f3)

    result = repository.fetch(session=5, batch=1, year=2016)
    assert len(result) == 2
    assert result[0].batch == 1
    assert result[0].session == 5
    assert result[0].year == 2016

    assert result[1].batch == 1
    assert result[1].session == 5
    assert result[1].year == 2016

    result_non_exists = repository.fetch(session=7, batch=1, year=1989)
    assert len(result_non_exists) == 0


