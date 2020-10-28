from random import sample
from string import ascii_letters, digits
from memento_pattern.Memento import Memento
from memento_pattern.SaveState import SaveState


# This creates a Memento with a snapshot of the state it's currently in (using the save function).
# Memento is then used to restore back to original state.

class Originator:
    # this state can hold whatever we want it to.
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: Current state set to:{self._state}")

    def generate_string_state(self) -> None:
        print("Originator: Generating string representation of state...")
        self._state = self.generate_random_string(40)
        print(f"Originator: State is currently set to: {self._state}")

    def generate_random_string(self, length: int = 20):
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return SaveState(self._state)

    def restore_state(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: State has been changed to: {self._state}")
