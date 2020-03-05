def hypervolume(length, *lengths):
  v = length
  for length in lengths:
    v *= length
  return v


print(hypervolume(2, 4))

print(hypervolume(2, 4, 6))

print(hypervolume(2, 4, 6, 8))

print(hypervolume(1))

print(hypervolume())

