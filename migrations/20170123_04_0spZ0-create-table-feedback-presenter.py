"""
Create table feedback_presenter
"""

from yoyo import step

__depends__ = {'20170123_03_WeBr8-create-table-participant'}

steps = [
    step("CREATE TABLE `feedback_presenter` ( \
            `id` int(11) NOT NULL AUTO_INCREMENT, \
            `presenter_id` int(11) NOT NULL, \
            `participant_id` int(11) NOT NULL, \
            `feedback_score_1` tinyint NOT NULL, \
            `feedback_score_2` tinyint NOT NULL, \
            `feedback_score_3` tinyint NOT NULL, \
            `feedback_score_4` tinyint NOT NULL, \
            `feedback_score_5` tinyint NOT NULL, \
            `total_score` tinyint NOT NULL, \
            `batch`, tinyint NOT NULL, \
            `year`, smallint NOT NULL, \
            `create_time` datetime(6) DEFAULT NULL, \
            `update_time` datetime(6) DEFAULT NULL, \
            PRIMARY KEY (`id`) \
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")
]
