store=[]
def sort_by_last_letter(strings):
  def last_letter(s):
      return s[-1]
  store.append(last_letter)
  print(last_letter)
  return sorted(strings, key=last_letter)

print(sort_by_last_letter(["hello", "from", "a", "local", "function"]))

# New local function is created each time it's parent function is called
"""
<function sort_by_last_letter.<locals>.last_letter at 0x104fe3ea0> <- diff
['a', 'local', 'from', 'function', 'hello']

<function sort_by_last_letter.<locals>.last_letter at 0x10a3b9ea0> <- diff
['a', 'local', 'from', 'function', 'hello']
"""



g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    inner()
outer() # global param local


