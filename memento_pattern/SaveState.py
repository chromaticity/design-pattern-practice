from memento_pattern.Memento import Memento
from datetime import datetime


# This SaveState uses our Memento interface.
class SaveState(Memento):

    def __init__(self, state: str):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date
