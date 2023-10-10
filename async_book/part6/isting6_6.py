import functools


def map_frequency(text: str) -> dict[str, int]:
    words = text.split(' ')
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] = frequencies[word] + 1
        else:
            frequencies[word] = 1
    return frequencies


def merge_dectionaries(first: dict[str, int],
                       second: dict[str, int]) -> dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged


lines = ["I know what I know",
         "I know that I know",
         "I don't know much",
         "They don't know much"]

mapped_result = [map_frequency(line) for line in lines]

for result in mapped_result:
    print(result)

print(functools.reduce(merge_dectionaries, mapped_result))
