import typing as t


# t.Iterable[int] - это протокол итераций
def iterate_by(numbers: t.Iterable[int]) -> None:
    for number in numbers:
        print(number)


iterate_by(range(1_000))
