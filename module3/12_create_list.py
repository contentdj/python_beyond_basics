# check_non_negative is not a decorator. 
# A decorator accepts a callable object and returns a callable object. 
# check_non_negative returns a function (a decorator)
def check_non_negative(index):
  # validator is a decorator
  def validator(f):
    def wrap(*args):
      if args[index] < 0:
        raise ValueError('Argument {} must be non-negative.'.format(index))
      return f(*args)
    return wrap
  return validator


@check_non_negative(1) # check second argument 
def create_list(value, size):
  return [value] * size

print(create_list(2, 1))
print(create_list(2, -1))

