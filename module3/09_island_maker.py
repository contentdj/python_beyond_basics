def escape_unicode(f):
  def wrap(*args, **kwargs):
    x = f(*args, **kwargs)
    return ascii(x)
  
  return wrap


class Trace:
  def __init__(self):
     self.enabled = True
  
  def __call__(self, f):
    def wrap(*args, **kwargs):
      if self.enabled:
        print('Calling {}'.format(f))
        return f(*args, **kwargs)
    
    return wrap

tracer = Trace()

@tracer
@escape_unicode
def chinese_island_maker(name):
  return name + " 台湾"


print(chinese_island_maker("taiwan"))



