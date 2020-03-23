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
    def create_empty(cls, owner_code, *args, **kwargs):
      return cls(owner_code, contents=None, *args, **kwargs)
    
    @classmethod
    def create_with_items(cls, owner_code, items, *args, **kwargs):
      return cls(owner_code, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()

class RefridgeratedShippingContainer(ShippingContainer):
  MAX_CELSIUS = 4.0

  # static method doesn't depend on class or instance values
  @staticmethod
  def _c_to_f(celsius):
    return celsius * 9 / 5 + 32
  
  @staticmethod
  def _f_to_c(farenheit):
    return (farenheit - 32) * 5 / 9

  def __init__(self, owner_code, contents, celsius):
    super().__init__(owner_code, contents)
    self.celsius = celsius
  
  @property
  def celsius(self):
    return self._celsius

  @celsius.setter
  def celsius(self, value):
    if value > RefridgeratedShippingContainer.MAX_CELSIUS:
      raise ValueError("Temperature {} is too hot!".format(value))
    self._celsius = value
  
  @property
  def farenheit(self):
    return RefridgeratedShippingContainer._c_to_f(self.celsius)
  
  @farenheit.setter
  def farenheit(self, value):
    self.celsius = RefridgeratedShippingContainer._f_to_c(value)

c5 = RefridgeratedShippingContainer.create_with_items("Items", ['i1', 'i2', 'i3'], celsius=-20.0)
print(c5.celsius)

c5.farenheit = 32
print(c5.celsius)

too_hot = RefridgeratedShippingContainer.create_with_items("Items", ['i1', 'i2', 'i3'], celsius=12)