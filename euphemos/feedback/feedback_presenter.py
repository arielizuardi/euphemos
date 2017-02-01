class FeedbackPresenter:

    def __init__(self,
                 _id=None,
                 batch,
                 year,
                 session,
                 participant,
                 participant_date,
                 group,
                 penguasaan_materi,
                 sistematika_penyajian,
                 metode_penyajian,
                 pengaturan_waktu,
                 penggunaan_alat_bantu,
                 nilai_keseluruhan,
                 positive_comment=None,
                 wish_comment=None,
                 created_at,
                 updated_at=None
                 ):

        self._id = _id
        self.batch = batch
        self.year = year
        self.session = session
        self.participant = participant
        self.participant_date = participant_date
        self.group = group
        self.penguasaan_materi = penguasaan_materi
        self.sistematika_penyajian = sistematika_penyajian
        self.metode_penyajian = metode_penyajian
        self.pengaturan_waktu = pengaturan_waktu
        self.penggunaan_alat_bantu = penggunaan_alat_bantu
        self.nilai_keseluruhan = nilai_keseluruhan
        self.positive_comment = positive_comment
        self.wish_comment = wish_comment
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self._id,
            "batch": self.batch,
            "year": self.year,
            "session": self.session,
            "participant": self.participant,
            "participant_date": self.participant_date,
            "grouo": self.group,
            "penguasaan_materi": self.penguasaan_materi,
            "sistematika_penyajian": self.sistematika_penyajian,
            "metode_penyajian": self.metode_penyajian,
            "pengaturan_waktu": self.pengaturan_waktu,
            "pengunaan_alat_bantu": self.penggunaan_alat_bantu,
            "nilai_keseluruhan": self.nilai_keseluruhan,
            "positive_comment": self.positive_comment,
            "wish_comment": self.wish_comment,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }