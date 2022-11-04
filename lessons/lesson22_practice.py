
col_data: dict[str, list[float]] = {
    "high": [77, 84, 78, 79, 65, 67, 74, 61, 55, 61],
    "low":  [67, 51, 64, 45, 43, 53, 56, 37, 34, 42],
    "rain": [.3, .2, .4, .8, 0., .2, .4, .5, .1, .1]
}


def less_than(col: list[float], threshold: float) -> list[bool]:
    """less than."""
    result: list[bool] = []
    for item in col:
        result.append(item < threshold)
    return result


def masked(col: list[float], mask: list[bool])-> list[float]:
    """masked."""
    result: list[float] = []
    for i in range(len(mask)):
        if mask[i]:
            result.append(col[i])
    return result


def mean(col: list[float]) -> float:
    """mean."""
    return sum(col)/len(col)


def not_mask(mask: list[bool]) -> list[bool]:
  result: list[bool] = []
  for item in mask:
    result.append(not item)
  return result

mask_a: list[bool] = less_than(col_data["high"], 80)
print(mask_a)
mask_b: list[bool] = not_mask(mask_a)
print(mask_b)

values: list[float] = masked(col_data["low"], mask_b)
print(mean(values))

print(len(masked(col_data["low"], less_than(col_data["low"], 32))))

print(less_than(col_data["high"], 65))

print(col_data["high"])

print(col_data["low"][1])