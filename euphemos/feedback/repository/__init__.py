class Repository:

    def store(self, feedback_presenter):
        """
        Store feedback presenter
        Args:
            feedback_presenter (euphemos.feedback_presenter.FeedbackPresenter) : FeedbackPresenter to be stored

        Returns:
            euphemos.feedback_presenter.FeedbackPresenter
        """
        raise NotImplementedError

    def fetch(self, session, batch, year, presenter=None):
        """
        Fetch feedback presenter
        Args:
            session:
            batch:
            year:
            presenter:

        Returns:
            list of euphemos.feedback_presenter.FeedbackPresenter
        """
        raise NotImplementedError
