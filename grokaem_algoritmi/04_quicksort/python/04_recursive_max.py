def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


print(sum([2, 5, 3]))


def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])
print(count([1, 2, 3]))


def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max([5,6,120]))


def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[int(len(list)/2)]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)




print(quicksort([1,9,5,11,88,44]))

