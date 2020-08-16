
class CommandInterface:

    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass


# Receivers contain the logic that our commands call on
class FileWriteReceiver:

    def write_to_file(self, filename: str, text: str):
        file_handle = open(filename, 'a')
        file_handle.write(text + "\n")
        file_handle.close()
        print(f"Message written to file: {filename} \n")


class FileUndoReceiver:

    def undo_write(self, filename: str):
        file_handle = open(filename)
        lines = file_handle.readlines()
        file_handle.close()
        write_file_handle = open(filename, 'w')
        write_file_handle.writelines([item for item in lines[:-1]])
        write_file_handle.close()
        print(f"Message undone from file {filename} \n")


# File write concrete command_pattern.
class FileWriteCommand(CommandInterface):

    def __init__(
            self,
            write_receiver: FileWriteReceiver,
            undo_receiver: FileUndoReceiver,
            filename,
            text=None
    ):
        self._text = text
        self._filename = filename
        self._writeReceiver = write_receiver
        self._undoReceiver = undo_receiver

    def execute(self) -> None:
        self._writeReceiver.write_to_file(self._filename, self._text)

    def undo(self) -> None:
        self._undoReceiver.undo_write(self._filename)


# lil invoker to call our commands at different intervals, in whatever order we want.
class Invoker:
    _on_command_start = None
    _on_command_end = None

    def set_on_start(self, command: FileWriteCommand) -> None:
        self._on_command_start = command

    def set_on_end(self, command: FileWriteCommand) -> None:
        self._on_command_end = command

    # We can organize our commands to run them in whatever order we want.
    def run_commands(self) -> None:
        print("Running command_pattern set on start...\n")
        if isinstance(self._on_command_start, FileWriteCommand):
            self._on_command_start.execute()

        print("Running command_pattern set on end...\n")
        if isinstance(self._on_command_end, FileWriteCommand):
            self._on_command_end.undo()

        print("Done executing all commands in Invoker. \n")

    """
    We normally wouldn't have functions like this, since Invoker is agnostic to implementation of these functions.
    These are just for debugging to show I can in fact write/undo to a file.
    """
    def run_write_command(self) -> None:
        self._on_command_start.execute()

    def run_undo_command(self) -> None:
        self._on_command_start.undo()
