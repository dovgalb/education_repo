from dataclasses import dataclass


@dataclass
class Computer:
    name: str
    memory_size: int


class SaveComputer:
    @staticmethod
    def save_to_file(computer: Computer):
        print(f'{computer} сохранен на диск')

    @staticmethod
    def save_to_db(computer: Computer):
        print(f'{computer} сохранен в БД')


if __name__ == "__main__":
    comp = Computer(name='MBP 15', memory_size=512)
    saver = SaveComputer()
    saver.save_to_file(computer=comp)