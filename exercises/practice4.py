
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index1 = 0
    index2 = 1
    largest_number = input[index1]
    while index2 < len(input):
        if input[index1] > input[index2]:
            largest_number = input[index1]
        else:
            largest_number = input[index2]
        index1 = index1 + 1
        index2 = index2 + 1
    if len(input) == 1:
        largest_number = input[index1]
    return largest_number


if len(list1) == 0 or len(list2) == 0:
    value = False