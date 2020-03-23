# decorator that returns ascii version of a function

def escape_unicode(f):
  def wrap(*args, **kwargs):
    x = f(*args, **kwargs)
    return ascii(x)
  
  return wrap

def chinese():
  return "中"

@escape_unicode
def ascii_chinese():
  return "中"

print(chinese())
print(ascii_chinese())