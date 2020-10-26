from memento_pattern.Originator import Originator


# This cannot see anything within the Memento.
# Makes sure that the Memento has full integrity.

class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def save_state(self) -> None:
        print("Caretaker: Saving state from Originator...")
        self._mementos.append(self._originator.save())

    def undo_action(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Reverting to state: {memento.get_name()}")
        try:
            self._originator.restore_state(memento)
        except Exception:
            self.undo_action()

    def show_history(self) -> None:
        print("Caretaker: Current list of mementos/save states")
        for memento in self._mementos:
            print(memento.get_name())
