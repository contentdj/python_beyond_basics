def color(red, green, blue, **kwargs):
  print('r=', red)
  print("g=", green)
  print("b=", blue)
  print(kwargs)

k = {'red': 21, 'green': 68, 'blue': 120, 'alpha': 52}
color(**k)

