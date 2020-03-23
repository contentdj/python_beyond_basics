class ShippingContainer(object):
    # class attribute
    next_serial = 1337

    @classmethod
    def _get_next_serial(cls):
      result = cls.next_serial
      cls.next_serial += 1
      return result

    # use class method as a factory method
    @classmethod
    def create_empty(cls, owner_code):
      return cls(owner_code, contents=None)
    
    @classmethod
    def create_with_items(cls, owner_code, items):
      return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()


c1 = ShippingContainer("YML", "books")
print(c1.owner_code)
print(c1.contents)
print(c1.serial)

c2 = ShippingContainer("MAE", "clothes")
print(c2.owner_code)
print(c2.contents)
print(c2.serial)

c3 = ShippingContainer.create_empty("Empty")
print(c3.owner_code)

c4 = ShippingContainer.create_with_items("Items", ['i1', 'i2', 'i3'])
print(c4.owner_code)
print(c4.contents)
