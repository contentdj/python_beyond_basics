class ShippingContainer(object):
    # class attribute
    next_serial = 1337

    @staticmethod
    def _get_next_serial():
      result = ShippingContainer.next_serial
      ShippingContainer.next_serial += 1
      return result

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
