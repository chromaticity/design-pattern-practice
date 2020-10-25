# main entry point for facade pattern stuff.

class Processor:
    # first subsystem
    def process(self):
        print("Processing...")


class Graphics:
    # second subsystem
    def display(self):
        print("Displaying...")


class Memory:
    # third subsystem
    def ioOperation(self):
        print("Reading and writing to memory...")


class Computer:

    def __init__(self):
        self.processor = Processor()
        self.graphics = Graphics()
        self.memory = Memory()

    def bootUp(self):
        self.processor.process()
        self.memory.ioOperation()
        self.graphics.display()


computer = Computer()
computer.bootUp()

if __name__ == '__main__':
    computer = Computer()
    computer.bootUp()
    pass
