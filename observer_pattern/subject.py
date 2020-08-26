# Subject interface for the subject.
class Subject:

    def attach(self, observer) -> None:
        pass

    def detach(self, observer) -> None:
        pass

    def notify(self) -> None:
        pass
