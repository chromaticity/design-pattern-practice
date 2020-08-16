from command_pattern.command import Invoker, FileWriteCommand, FileUndoReceiver, FileWriteReceiver;

"""
For the sake of simplicity, all classes will be done in a single file.
For example, Command pattern is in the command_pattern directory, inside of the
command_pattern.py file. We will import classes we need.

This file will be our 'main', where we run all of the classes.
"""

# Command Pattern
# Call invoker
invoker = Invoker()

# Call all receivers. All of them are required whether you're deleting/adding.
file_write_receiver = FileWriteReceiver()
file_undo_receiver = FileUndoReceiver()

"""
Yeah I know this is stupid but it shows we can run our commands through the invoker
to write, and immediately undo what was written to the file.
"""
invoker.set_on_start(FileWriteCommand(file_write_receiver, file_undo_receiver, 'output.txt', 'This is a new line.'))
invoker.set_on_end(FileWriteCommand(file_write_receiver, file_undo_receiver, 'output.txt'))
invoker.run_commands()

# These show that we can indeed just call the write/undo to the file.
invoker.set_on_start(FileWriteCommand(file_write_receiver, file_undo_receiver, 'output.txt', 'This is a dummy line'))
invoker.run_write_command()

invoker.set_on_start(FileWriteCommand(file_write_receiver, file_undo_receiver, 'output.txt', 'This line will disappear...'))
invoker.run_write_command()

invoker.set_on_start(FileWriteCommand(file_write_receiver, file_undo_receiver, 'output.txt'))
invoker.run_undo_command()
