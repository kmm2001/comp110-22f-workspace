
def average_grades(grades: dict[str, list[int]]) -> dict[str, float]:
    """Return averages."""
    averages: dict[str, float] = {}
    for student in grades:
        total: int = 0
        for grade in grades[student]:
            total = total + grade
        averages[student] = total/len(grades[student])
    return averages


def odd_and_even(list1: list[int]) -> list[int]:
    """Find the odd elements with even indexes."""
    i: int = 0
    list2: list[int] = []
    while i < len(list1):
        if list1[i] % 2 == 1 and i % 2 == 0:
            list2.append(list1[i])
        i = i + 1
    return list2


def odd_and_even2(list1: list[int]) -> list[int]:
    """Find the odd elements with even indexes."""
    i: int = 0
    list2: list[int] = []
    for item in list1:
        if item % 2 ==1 and i % 2 == 0:
            list2.append(list1[i])
        i = i + 1
    return list2


def fn(d: dict[str, int]) -> None:
    """Print."""
    for key in d:
        print(key)



def fn2(dict1: dict[str, int]) -> dict[str, int]:
    """Test."""
    i: int = 0
    while i < len(dict1):
        dict1[i] = dict1[i]
    i = i + 1
    return dict1
