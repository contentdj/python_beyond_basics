class ShippingContainer(object):
    # class attribute
    next_serial = 1337

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    @classmethod
    def _get_next_serial(cls):
      result = cls.next_serial
      cls.next_serial += 1
      return result

    # use class method as a factory method
    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
      return cls(owner_code, length_ft, contents=None, *args, **kwargs)
    
    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
      return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, length_ft, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.length_ft = length_ft
        self.serial = ShippingContainer._get_next_serial()
    
    @property
    def volume_ft3(self):
      return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

class RefridgeratedShippingContainer(ShippingContainer):
  MAX_CELSIUS = 4.0
  FRIDGE_VOLUME_FT3 = 100

  # static method doesn't depend on class or instance values
  @staticmethod
  def _c_to_f(celsius):
    return celsius * 9 / 5 + 32
  
  @staticmethod
  def _f_to_c(farenheit):
    return (farenheit - 32) * 5 / 9

  def __init__(self, owner_code, length_ft, contents, celsius):
    super().__init__(owner_code, length_ft, contents)
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
  
  @property
  def volume_ft3(self):
    """ Overwritten """
    return super().volume_ft3 - RefridgeratedShippingContainer.FRIDGE_VOLUME_FT3

class HeatedShippingContainer(RefridgeratedShippingContainer):
  MIN_CELSIUS = -20.0

  @RefridgeratedShippingContainer.celsius.setter
  def celsius(self, value):
    if value < HeatedShippingContainer.MIN_CELSIUS:
      raise ValueError("Temperature {} is too cold".format(value))
    RefridgeratedShippingContainer.celsius.fset(self, value)
  
c1 = ShippingContainer.create_empty("Empty", length_ft=20)
print(c1.volume_ft3)

c2 = RefridgeratedShippingContainer.create_empty("Empty", length_ft=20, celsius=-10)
print(c2.volume_ft3)

heated = HeatedShippingContainer.create_empty("Heated", length_ft=20, celsius=-15)
print(heated.celsius)

heated = HeatedShippingContainer.create_empty("Heated", length_ft=20, celsius=-25)
print(heated.celsius)
