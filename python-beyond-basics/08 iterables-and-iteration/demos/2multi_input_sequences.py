sizes = ['small', 'medium', 'large']
colors = ['lavendar', 'teal', 'burnt orange']
animals = ['koala', 'platypus', 'salamander']

def combine(size, color, animal):
  return f"{size}, {color}, {animal}"

print(list(map(combine, sizes, colors, animals)))

import itertools
def combine2(quantity, size, color, animal):
  return f"{quantity} x {size}, {color}, {animal}"

# Terminate as soon as the first sequence terminates
print(list(map(combine2, itertools.count(), sizes, colors, animals)))

