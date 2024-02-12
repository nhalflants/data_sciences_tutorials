from typing import List
import sys

print(sys.path)


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

# list_avg(123)


# def double(x):
#     return x * 2

# seq = [1, 3, 5, 8]
# # doubled = [x * 2 for x in seq]
# # doubled = [double(x) for x in seq]
# doubled = map(double, seq)
# print(doubled)

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = (90, 30, 50, 40)

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Nat")
print(student.average())

class Device:
    def __init__(self, name, connected_by) -> None:
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self) -> str:
        return f"Device {self.name!r}"

    def disconnect(self):
        self.connected = False
        print(self.connected)

class Printer(Device):
    def __init__(self, name, connected_by, capacity) -> None:
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("out")
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages

printer = Printer("Printer XXX", "USB", 500)
# print(printer)

# printer.print(20)

# print(printer)

# printer.disconnect()
# printer.print(20)