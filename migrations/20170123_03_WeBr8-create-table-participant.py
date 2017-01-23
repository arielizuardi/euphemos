"""
Create table participant
"""

from yoyo import step

__depends__ = {'20170123_02_vFzZm-create-table-presenter'}

steps = [
    step("CREATE TABLE `participant` ( \
            `id` int(11) NOT NULL AUTO_INCREMENT, \
            `name` varchar(50) NOT NULL DEFAULT '' , \
            `date` varchar(50) NOT NULL DEFAULT '' , \
            `email` varchar(50) NOT NULL DEFAULT '', \
            `DOB` datetime(6) DEFAULT NULL, \
            `phone_number` VARCHAR(20) DEFAULT NULL, \
            `join_at` datetime(6) DEFAULT NULL, \
            `create_time` datetime(6) DEFAULT NULL, \
            `update_time` datetime(6) DEFAULT NULL, \
            PRIMARY KEY (`id`), \
            UNIQUE KEY `email` (`email`) \
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")
]
