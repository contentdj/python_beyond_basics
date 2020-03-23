def enclosing():
  def local_func():
    print('local func')
  return local_func

lf = enclosing()
# invoke the function
lf()