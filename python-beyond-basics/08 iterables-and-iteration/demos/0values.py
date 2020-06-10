print([(outer,inner) for outer in range(5) for inner in range(3)])
"""
for outer in range(5):
  for inner in range(3)
"""

values = [x / (x - y) for x in range(100) if x > 50 for y in range(100) if x - y != 0]

values = [x / (x - y)
          for x in range(100)
          if x > 50
          for y in range(100)
          if x - y != 0]

values = []
for x in range(100):
    if x > 50:
        for y in range(100):
            if x - y != 0:
                values.append(x / (x - y))