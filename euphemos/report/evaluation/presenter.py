class PresenterEvaluationReport:

    def __init__(
            self,
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
    ):
        self.batch = batch
        self.year = year
        self.session = session
        self.presenter = presenter
        self.avg_penguasaan_materi = avg_penguasaan_materi
        self.avg_sistematika_penyajian = avg_sistematika_penyajian
        self.avg_metode_penyajian = avg_metode_penyajian
        self.avg_pengaturan_waktu = avg_pengaturan_waktu
        self.avg_penggunaan_alat_bantu = avg_penggunaan_alat_bantu
        self.positive_comment = positive_comment
        self.improvement_comment = improvement_comment


    def to_dict(self):
        return {
            "batch": self.batch,
            "year": self.year,
            "session" : self.session,
            "presenter": self.presenter,
            "avg_penguasaan_materi": self.avg_penguasaan_materi,
            "avg_sistematika_penyajian" : self.avg_sistematika_penyajian,
            "avg_metode_penyajian": self.avg_metode_penyajian,
            "avg_pengaturan_waktu": self.avg_pengaturan_waktu,
            "avg_penggunaan_alat_bantu": self.avg_penggunaan_alat_bantu
            "positive_comment": self.positive_comment,
            "improvement_comment": self.improvement_comment
        }