# Observer interface for all of our observers.
from typing import List


class Observer:

    def update(self, subject: Subject) -> None:
        pass


# Subject interface for the subject.
class Subject:

    def attach(self, observer: Observer) -> None:
        pass

    def detach(self, observer: Observer) -> None:
        pass

    def notify(self) -> None:
        pass


# message board; notifies students of new assignments and stuff
class MessageBoard(Subject):
    # Message that will be given to all students
    message: str = None

    # List of all students; subscribed to the MessageBoard
    _allObservers: List[Observer] = []

    def attach(self, student: Observer) -> None:
        self._allObservers.append(student)

    def detach(self, student: Observer) -> None:
        self._allObservers.remove(student)

    def notify(self) -> None:
        for student in self._allObservers:
            student.update(self)

    def send_message(self, message) -> None:
        print("Sending message...\n")
        self.message = message
        self.notify()
        print("Message sent, users notified.\n")


class Student(Observer):
    def update(self, subject: MessageBoard) -> None:
        if subject.message == "ping":
            print("Student reacted to ping event... \n")


if __name__ == "__main__":

    message_board = MessageBoard()
    student = Student()

    message_board.attach(student)

    message_board.send_message('ping')

    message_board.detach(student)