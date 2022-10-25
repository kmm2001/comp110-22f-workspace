
x: int = 1

def function(y: int) -> int:
  return x + y

print(function(x + 1))


i: int = 0
ys: list[int] = [110, 120]
while i < len(ys):
  y: int = ys[i]
  print(y)
  i += 1