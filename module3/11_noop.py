def noop(f):
  def noop_wrapper():
    return f()
  return noop_wrapper

def hello():
  "Print a well-known message."
  print("Hello, world!")

print(hello.__name__)
print(hello.__doc__)
# print(help(hello))

@noop
def hello_decorated():
  "Print a well-known message."
  print("Hello, world!")

# __name__ and __doc__ is now not working properly anymore
print(hello_decorated.__name__)
print(hello_decorated.__doc__)
# print(help(hello_decorated))


# functools.wraps comes to the rescue. It properly updates metadata on the wrapped functions.

import functools
def noop_proper(f):
  @functools.wraps(f)
  def noop_wrapper():
    return f()
  return noop_wrapper

@noop_proper
def hello_decorated_proper():
  "Print a well-known message proper."
  print("Hello, world!")

# __name__ and __doc__ is now not working properly anymore
print(hello_decorated_proper.__name__)
print(hello_decorated_proper.__doc__)
