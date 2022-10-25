def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], return a dict[str, str] that inverts the keys and the values."""
    dict2: dict[str, str]
    for key, value in dict1.items():
        dict2[value].append(key)
    return dict2


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], return a dict[str, str] that inverts the keys and the values."""
    dict2 = {v: k for k, v in dict1.items()}
    return dict2


def favorite_color(dict1: dict[str, str]) -> str:
    """Return a str which is the color that appears most frequently."""  
    dict1: dict[str, str] = {}
    list1: list[str] = []
    count: 0
    dict2: dict[str, int] = {}
    common: None
    for key in dict1:
        if dict2[key] >= count:
            count = dict[key]
            common = key
    return common


#def invert(dict1: dict[str, str]) -> dict[str, str]:
    #"""Given a dictionary of [str, str], return a dict[str, str] that inverts the keys and the values."""
    #dict2 = {value: key for key, value in dict1.items()}
    #return dict2




#def favorite_color(dict1: dict[str, str]) -> str:
    #"""Return a str which is the color that appears most frequently."""  
    #dict1: dict[str, str] = {}
    #list1: list[str] = []
    #count: 0
    #dict2: dict[str, int] = {}
    #common: None
    #for key in dict1:
        #if dict2[key] >= count:
            #count = dict[key]
            #common = key
    #return common


#def invert(dict1: dict[str, str]) -> dict[str, str]:
    #"""Given a dictionary of [str, str], return a dict[str, str] that inverts the keys and the values."""
    #dict2 = {value: key for key, value in dict1.items()}
    #return dict2


# Example looping over the keys of a dict
#for key in schools:
    #print(f"Key: {key} -> Value: {schools[key]}")

#for school in schools:
    #print(f"Key: {school} -> Value: {schools[school]}")




def max(input: list[int]) -> int:
    """Given a list of ints, max should return the largest in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index1 = 0
    largest_number = input[0]
    while index1 < len(input):
        if input[index1] > largest_number:
            largest_number = input[index1]
        else:
            largest_number = largest_number
        index1 = index1 + 1
    return largest_number