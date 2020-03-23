message = "global"

def enclosing():
  message = "enclosing"

  def local():
    message = 'local'
  print('enclosing message:', message)
  local()
  print('enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)


# use global keyword
print("==== Global Keyword ====")
message = "global"

def enclosing():
  message = "enclosing"

  def local():
    global message
    message = 'local'
  print('enclosing message:', message)
  local()
  print('enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)


# use nonlocal keyword
print("==== Nonlocal Keyword ====")
message = "global"

def enclosing():
  message = "enclosing" # modified

  def local():
    nonlocal message
    message = 'local'
  print('enclosing message:', message)
  local()
  print('enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)



