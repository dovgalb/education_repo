import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=12))


@dataclass(match_args=True)
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id, init=False, compare=False)
    _search_str: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_str = f'{self.name} {self.address}'


def main() -> None:
    person = Person(name='John', address='123 Main St')
    person2 = Person(name='John', address='124 Main St')
    print(person2 == person)
    print(person)


if __name__ == '__main__':
    main()
