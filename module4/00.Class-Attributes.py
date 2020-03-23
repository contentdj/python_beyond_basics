class ShippingContainer(object):
    # class attribute
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1


c1 = ShippingContainer("YML", "books")
print(c1.owner_code)
print(c1.contents)
print(c1.serial)

c2 = ShippingContainer("MAE", "clothes")
print(c2.owner_code)
print(c2.contents)
print(c2.serial)

# zen of python
# import this