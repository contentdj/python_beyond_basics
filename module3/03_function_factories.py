def raise_to(exp):
  def raise_to_exp(x):
    return pow(x, exp)
  return raise_to_exp

square = raise_to(2)
print(square.__closure__) # return to 2

print(square(2))
print(square(4))

cube = raise_to(3)
print(cube(3))
