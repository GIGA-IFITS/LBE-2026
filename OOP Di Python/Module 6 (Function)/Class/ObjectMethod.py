class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self): # Object method
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# 1.    Object methods are functions defined in a class that 
#       can be called on an object created from that class.

# 2.    They can access and modify the object’s attributes and 
#       perform actions relevant to the object.