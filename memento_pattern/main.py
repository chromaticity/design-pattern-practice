# Run everything lmao
from memento_pattern.Caretaker import Caretaker
from memento_pattern.Originator import Originator

if __name__ == "__main__":
    originator = Originator("FUCK")
    caretaker = Caretaker(originator)

    caretaker.save_state()
    originator.generate_string_state()

    caretaker.save_state()
    originator.generate_string_state()

    caretaker.save_state()
    originator.generate_string_state()

    print()
    caretaker.show_history()

    print("\n Rolling back to previous save state...")
    caretaker.undo_action()

    print("\n Rolling back to previous state again...")
    caretaker.undo_action()
