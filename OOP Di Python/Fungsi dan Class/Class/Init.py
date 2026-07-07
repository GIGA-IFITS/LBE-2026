class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
x2 = Person("Mandy", 19)

print(p1.name)
print(p1.age)
print(x2.name)
print(x2.age)

# All classes have a function called __init__(), which is always 
# executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created.