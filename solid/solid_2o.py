from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Computer:
    name: str
    memory_size: int


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


if __name__ == "__main__":
    comp = Computer(name='MBP 15', memory_size=512)
    saver = SaveComputerToDB()
    saver.save(comp)
