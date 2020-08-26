from observer_pattern.subject import Subject
from observer_pattern.observer import Observer
from typing import List


# message board; notifies students of new assignments and stuff
class MessageBoard(Subject):
    # Message that will be given to all students
    message: str = None

    # List of all students; subscribed to the MessageBoard
    _allObservers: List[Observer] = []

    def attach(self, student_observer: Observer) -> None:
        self._allObservers.append(student_observer)

    def detach(self, student_observer: Observer) -> None:
        self._allObservers.remove(student_observer)

    def notify(self) -> None:
        for student_observer in self._allObservers:
            student_observer.update(self)

    def send_message(self, message) -> None:
        print("Sending message...\n")
        self.message = message
        self.notify()
        print("Message sent, users notified.\n")
