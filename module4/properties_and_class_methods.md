# Properties and Class Methods

## Class Attributes

Prefer to mention class attributes via class name not `self`:
```python
class ShippingContainer(object):

    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
```

# import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


## `staticmethod` vs `classmethod`

### `staticmethod`

- No access needed to either class or instance objects
- Most likely an implementation detail of the class
- May be able to be moved to become a module-scope function

### `classmethod`

- Requires access to the class object to call other class methods

```python
class ShippingContainer:

    next_serial = 1337

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    # ...
```

# 03.Static-Methods-with-Inheritance

Static methods in python can be overwritten by subclasses



### `property`

```python
class Example:

    def __init__(self):
        self._p = 1

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        self._p = value
```
