"""
Create table presenter
"""

from yoyo import step

__depends__ = {'20170123_01_gSXlp-create-table-facilitator'}

steps = [
    step("CREATE TABLE `presenter` ( \
            `id` int(11) NOT NULL AUTO_INCREMENT, \
            `name` varchar(50) NOT NULL DEFAULT '' , \
            `image_url` varchar(200) NOT NULL DEFAULT '', \
            `create_time` datetime(6) DEFAULT NULL, \
            `update_time` datetime(6) DEFAULT NULL, \
            PRIMARY KEY (`id`) \
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")
]
