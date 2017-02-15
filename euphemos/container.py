from euphemos.exceptions import ContainerPropertyAlreadySet


class Container:
    @property
    def db_connection(self):
        """

        Returns:

        """
        return getattr(self, '_db_connection', None)

    @db_connection.setter
    def db_connection(self, db_conn):
        """

        Returns:

        """
        if self.db_connection is not None:
            raise ContainerPropertyAlreadySet

        setattr(self, '_db_connection', db_conn)

    @property
    def feedback_presenter_repository(self):
        """
        Returns:
            euphemos.feedback.repository.Repository
        """
        return getattr(self, '_feedback_presenter_repository', None)

    @feedback_presenter_repository.setter
    def feedback_presenter_repository(self, repository):
        """
        Args:
            repository (euphemos.feedback.repository.Repository):
        Raises:
            europa.exceptions.ContainerPropertyAlreadySet
        """
        if self.feedback_presenter_repository is not None:
            raise ContainerPropertyAlreadySet

        setattr(self, '_feedback_presenter_repository', repository)

container = Container()
