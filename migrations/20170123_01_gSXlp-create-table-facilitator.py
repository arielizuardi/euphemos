"""
Create table facilitator
"""

from yoyo import step

__depends__ = {'__init__'}

steps = [
    step("CREATE TABLE `facilitator` ( \
            `id` int(11) NOT NULL AUTO_INCREMENT, \
            `name` varchar(50) NOT NULL DEFAULT '' , \
            `date` varchar(50) NOT NULL DEFAULT '' , \
            `email` varchar(50) NOT NULL DEFAULT '', \
            `image_url` varchar(200) NOT NULL DEFAULT '', \
            `DOB` datetime(6) DEFAULT NULL, \
            `join_at` datetime(6) DEFAULT NULL, \
            `create_time` datetime(6) DEFAULT NULL, \
            `update_time` datetime(6) DEFAULT NULL, \
            PRIMARY KEY (`id`), \
            UNIQUE KEY `email` (`email`) \
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")
]
