def trace(f, *args, **kwargs):
  print("args =", args)
  print("kwargs =", kwargs)
  # forwarding to f
  result = f(*args, **kwargs)
  print("result =", result)
  return result

assert int("ff", base=16) == trace(int, "ff", base=16)

