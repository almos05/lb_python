import re
import random
from abc import ABC, abstractmethod


class Field:
    def __init__(self, size: (tuple, list)):
        rows, cols = size
        self.size = size
        self.matrix = [["_" for _ in range(cols)] for _ in range(rows)]

    def out(self):
        print("\n".join("  ".join(row) for row in self.matrix))

    def gen(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                rnd = random.randint(1, 100)
                if rnd <= 60:
                    self.matrix[i][j] = '•'
                elif rnd <= 75:
                    self.matrix[i][j] = '█'
                elif rnd <= 90:
                    self.matrix[i][j] = '$'
                else:
                    self.matrix[i][j] = 'ø'


class Unit(ABC):
    @abstractmethod
    def __init__(self):
        self._money = None
        self._lives = None
        self.field = None
        self._pos = None
        self._icon_unit = None
        self._commands = None

    @abstractmethod
    def move(self, command):
        pass

    def _check_and_print_field(self, command):
        self.field.matrix[self._pos[0]][self._pos[1]] = '•'

        temp_pos = self._pos

        self._pos = self._commands[command](*self._pos)
        if ((not (0 <= self._pos[0] < self.field.size[0]) or not (0 <= self._pos[1] < self.field.size[1])) or
                self.field.matrix[self._pos[0]][self._pos[1]] == '█'):
            self._pos = temp_pos

        if self.field.matrix[self._pos[0]][self._pos[1]] == '$':
            self._money += 1

        if self.field.matrix[self._pos[0]][self._pos[1]] == 'ø':
            self._lives -= 1

        if self._lives == 0:
            print(f'Game over\nMoney: {self._money}')
            exit()

        print(f"\tMoney: {self._money}\t Lives: {self._lives}")

        self.field.matrix[self._pos[0]][self._pos[1]] = self._icon_unit


class Rook(Unit):
    def __init__(self, field):
        self._money = 0
        self._lives = 2
        self.field = field
        self._pos = (0, 0)
        self._icon_unit = "❤"
        self._commands = {
            'w': lambda x, y: (x - 1, y),
            'a': lambda x, y: (x, y - 1),
            's': lambda x, y: (x + 1, y),
            'd': lambda x, y: (x, y + 1)
        }
        self.field.matrix[self._pos[0]][self._pos[1]] = self._icon_unit

    def move(self, command):
        if command not in self._commands.keys():
            return None

        self._check_and_print_field(command)


class Teleport(Unit):
    def __init__(self, field):
        self._money = 0
        self._lives = 2
        self.field = field
        self._pos = (0, 0)
        self._icon_unit = "❦"
        self.field.matrix[self._pos[0]][self._pos[1]] = self._icon_unit

    def move(self, command):
        if match := re.match(r'\(?(\d+),? *(\d+)\)?', command):
            self._commands = {"yes": lambda x, y: (int(match[2]), int(match[1]))}

        if not match:
            self._commands = {"yes": lambda x, y: (x, y)}

        self._check_and_print_field("yes")