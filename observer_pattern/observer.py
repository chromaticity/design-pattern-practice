# Observer interface for all of our observers.
class Observer:

    def update(self) -> None:
        pass


# Subject interface for the subject.
class Subject:

    def attach(self, observer: Observer) -> None:
        pass

    def detach(self, observer: Observer) -> None:
        pass

    def notify(self) -> None:
        pass


# Now, make your subjects/observers and have them fuck with each other....