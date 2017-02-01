"""
create table feedback_presenter
"""

from yoyo import step

__depends__ = {'__init__'}

steps = [
    step("CREATE TABLE `feedback_presenter` ( \
          `id` int(11) NOT NULL AUTO_INCREMENT, \
          `batch` int(11) DEFAULT NULL, \
          `year` int(11) DEFAULT NULL, \
          `session` int(11) DEFAULT NULL, \
          `presenter` varchar(100) DEFAULT NULL, \
          `participant` varchar(100) DEFAULT NULL, \
          `participant_date` varchar(100) DEFAULT NULL, \
          `group` varchar(255) DEFAULT NULL, \
          `penguasaan_materi` int(11) DEFAULT NULL, \
          `sistematika_penyajian` int(11) DEFAULT NULL, \
          `metode_penyajian` int(11) DEFAULT NULL, \
          `pengaturan_waktu` int(11) DEFAULT NULL, \
          `penggunaan_alat_bantu` int(11) DEFAULT NULL, \
          `nilai_keseluruhan` int(11) DEFAULT NULL, \
          `positive_comment` text, \
          `wish_comment` text, \
          `created_at` datetime DEFAULT NULL, \
          `updated_at` datetime DEFAULT NULL, \
          PRIMARY KEY (`id`), \
          KEY `batch_year` (`batch`,`year`) \
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1; \
    ")
]
