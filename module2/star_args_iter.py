def hypervolume(*lengths):
  i = iter(lengths)
  
  # get lengths[0]
  v = next(i)
  
  for length in i:
    v *= length
  return v


print(hypervolume(2, 4))

print(hypervolume(2, 4, 6))

print(hypervolume(2, 4, 6, 8))

print(hypervolume(1))

print(hypervolume())

