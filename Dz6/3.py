class MyClass:
    def __init__(self, value=None):
        if value is None:
            self._value = "Default Value"
        elif isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Invalid value type. Expected str or None.")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Invalid value type. Expected str.")

obj1 = MyClass()
print(obj1.value)

obj2 = MyClass("Custom Value")
print(obj2.value)

obj2.value = "New Value"
print(obj2.value)