class Analyzer:
    """ analyzes various UX KPIs
    """

    def __init__(self, url: str) -> None:
        self.url: str = url

    def get_security(self) -> float:
        """ check security of the given website
        """
        return 0.5
