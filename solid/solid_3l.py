from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Computer:
    name: str
    memory_size: int

    def set_data(self, name: str):
        self.name = name


class SaveInterface(ABC):
    @abstractmethod
    def save(self, cmp: Computer):
        pass


class SaveComputerToFile(SaveInterface):
    def save(self, cmp: Computer):
        print(f'{comp} сохранен в файл')


class SaveComputerToDB(SaveInterface):
    def save(self, cmp: Computer):
        print(f'{cmp} - сохранен в базу данных')


class OmenHP(Computer):
    def set_data(self, name: str, memory_size: int):
        self.name = name
        self.memory_size = 8000


if __name__ == "__main__":
    comp = Computer(name='MBP 15', memory_size=512)
    saver = SaveComputerToDB()
    saver.save(comp)
