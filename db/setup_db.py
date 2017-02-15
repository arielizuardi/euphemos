from euphemos.feedback.repository.sql import feedback_presenter_metadata
from euphemos.container import container


def create_tables(sql_engine):
    feedback_presenter_metadata.create_all(sql_engine)


if __name__ == "__main__":
    engine = container.db_connection
    create_tables(engine=engine)
