# Observer interface for all of our observers.
from observer_pattern.message_board import MessageBoard
from observer_pattern.student import Student
from observer_pattern.teacher import Teacher

if __name__ == "__main__":

    message_board = MessageBoard()
    student = Student()
    teacher = Teacher()

    message_board.attach(student)
    message_board.attach(teacher)

    # ping for students
    message_board.send_message('ping')
    # pong for teachers
    message_board.send_message('pong')

    message_board.detach(student)
    message_board.detach(teacher)
