class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p2 = Person("Alex", 25)
p3 = Person("James", 26)
p4 = Person("Rose", 30)
p5 = Person("Joy", 33)
p6 = None # Nothing inside p6

# 'del p1.name' the function will cause an error 
# because the class attribute is empty.
del p2.age # Delete age atribut in p2
del p3 # Delete the entire p3

p1.myfunc()