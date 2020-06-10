from functools import reduce

import operator
print(reduce(operator.add, [1,2,3,4,5]))

print(reduce(operator.xor, [0, 1]))

def mul(x, y):
  print(f"{x} x {y}")
  return x * y

print(reduce(mul, range(1, 10)))

# accepts an intial value
vals = []
print(reduce(operator.add, vals, 0))