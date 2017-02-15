from sqlalchemy import select
from euphemos.feedback.repository import Repository
from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData
from euphemos.feedback.feedback_presenter import FeedbackPresenter


class SQLRepository(Repository):

    def __init__(self, sql_engine):
        self.sql_engine = sql_engine

    def store(self, feedback_presenter):
        pass

    def fetch(self, session, batch, year, presenter=None):
        conn = self.sql_engine.connect()

        stmt = select([feedback_presenter_table]).\
            where(feedback_presenter_table.c.session == session).\
            where(feedback_presenter_table.c.batch == batch).\
            where(feedback_presenter_table.c.year == year)

        sql_result = conn.execute(stmt).fetchall()

        return [unmarshal(row) for row in sql_result]


def unmarshal(row):
    feedback_presenter = FeedbackPresenter(
                _id=row['id'],
                batch=row['batch'],
                year=row['year'],
                session=row['session'],
                presenter=row['presenter'],
                participant=row['participant'],
                participant_date=row['participant_date'],
                group=row['group'],
                penguasaan_materi=row['penguasaan_materi'],
                sistematika_penyajian=row['sistematika_penyajian'],
                metode_penyajian=row['metode_penyajian'],
                pengaturan_waktu=row['pengaturan_waktu'],
                penggunaan_alat_bantu=row['penggunaan_alat_bantu'],
                nilai_keseluruhan=row['nilai_keseluruhan'],
                positive_comment=row['positive_comment'],
                wish_comment=row['wish_comment'],
                created_at=row['created_at'],
                updated_at=row['updated_at']
            )

    return feedback_presenter

feedback_presenter_table_name = 'feedback_presenter'
feedback_presenter_metadata = MetaData()
feedback_presenter_table = Table(feedback_presenter_table_name, feedback_presenter_metadata,
                                 Column('id', Integer, primary_key=True),
                                 Column('batch', Integer),
                                 Column('year', Integer),
                                 Column('session', Integer),
                                 Column('presenter', String),
                                 Column('participant', String),
                                 Column('participant_date', String),
                                 Column('group', String),
                                 Column('penguasaan_materi', Integer),
                                 Column('sistematika_penyajian', Integer),
                                 Column('metode_penyajian', Integer),
                                 Column('pengaturan_waktu', Integer),
                                 Column('penggunaan_alat_bantu', Integer),
                                 Column('nilai_keseluruhan', Integer),
                                 Column('positive_comment', String),
                                 Column('wish_comment', String),
                                 Column('created_at', DateTime),
                                 Column('updated_at', DateTime)
                                 )

