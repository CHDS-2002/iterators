import os

os.system('COLOR B')


class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step, pointer):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = pointer

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step

        if abs(self.pointer) > abs(self.stop):
            return self


try:
    iter1 = Iterator(100, 200, 0)

    for i in iter1:
        print(i, end=' ')

except StepValueError:
    print('Шаг не может быть равен 0')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')

print()

for i in iter3:
    print(i, end=' ')

print()

for i in iter4:
    print(i, end=' ')

print()

for i in iter5:
    print(i, end=' ')

print()

try:
    os.system('PAUSE')
except:
    os.system('CLS')
