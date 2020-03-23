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

class IslandMaker:
  def __init__(self, suffix):
    self.suffix = suffix
  
  @tracer
  def make_island(self, name):
    return name + self.suffix

im = IslandMaker('yo')
print(im.make_island("Ireland "))