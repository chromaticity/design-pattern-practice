from observer_pattern.observer import Observer
from observer_pattern.message_board import MessageBoard


class Teacher(Observer):
    def update(self, subject: MessageBoard) -> None:
        if subject.message == "pong":
            print("Teacher reacted to pong event... \n")
