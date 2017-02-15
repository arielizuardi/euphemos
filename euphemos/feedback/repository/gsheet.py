from euphemos.feedback.feedback_presenter import FeedbackPresenter
from euphemos.feedback.repository import Repository
from datetime import datetime

DATETIME_FORMAT = '%m/%d/%Y %H:%M:%S'


class GsheetRepository(Repository):

    def __init__(self, service, spreadsheet_id, range_name):
        """

        Args:
            service:
            spreadsheet_id:
            range_name:
        """
        self.service = service
        self.spreadsheet_id = spreadsheet_id
        self.range_name = range_name

    def store(self, feedback_presenter):
        pass

    def fetch(self, session, batch, year, presenter=None):
        pass

    def fetchall(self):
        result = self.service\
            .spreadsheets()\
            .values()\
            .get(spreadsheetId=self.spreadsheet_id, range=self.range_name)\
            .execute()

        values = result.get('values', [])

        if not values:
            return []

        return [self.unmarshal(row) for row in values]

    def unmarshal(self, row):

        feedback_presenter = FeedbackPresenter(
            _id=None,
            batch=0,
            year=0,
            session=0,
            presenter='',
            participant=row[1],
            participant_date=row[2],
            group=row[3],
            penguasaan_materi=row[4],
            sistematika_penyajian=row[5],
            metode_penyajian=row[6],
            pengaturan_waktu=row[7],
            penggunaan_alat_bantu=row[8],
            nilai_keseluruhan=row[9],
            positive_comment=row[10],
            wish_comment=row[11],
            created_at=datetime.strptime(row[0], DATETIME_FORMAT),
            updated_at=None
        )

        return feedback_presenter

