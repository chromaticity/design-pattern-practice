from observer_pattern.observer import Observer
from observer_pattern.message_board import MessageBoard


class Student(Observer):
    def update(self, subject: MessageBoard) -> None:
        if subject.message == "ping":
            print("Student reacted to ping event... \n")
