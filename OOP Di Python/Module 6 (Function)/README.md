# Module 6: Functions and Classes in Python

This module covers two major building blocks of Python programming. First, we explore **Functions** to create reusable blocks of logic and handle memory references. Then, we dive into **Object-Oriented Programming (OOP)** to structure code using Classes and Objects.

---

## Part 1: Functions

Functions allow you to wrap code into a named block that can be called whenever needed.

### 1. Basic Functions (`Function.py`)
To define a function in Python, use the `def` keyword.

```python
def printf():
    print("This is a function.")

printf() # Calling the function

```

### 2. Arguments and Parameters (`Argument.py` & `Math.py`)

You can pass data into functions using parameters.

* **Parameter**: The variable listed inside the parentheses in the function definition.
* **Argument**: The value that is sent to the function when it is called.

```python
# 1. Single Argument
def my_function(fname):
  print(fname + " Refsnes")

# 2. Multiple Arguments
def math(a, b):
    c = a + b
    print("Hasil pertambahannya adalah", c)

# Getting input for the function
a, b = map(int, input("Masukkan 2 angka: ").split())
math(a, b)

```

### 3. Arbitrary Arguments (`Pointer.py`)

If you don't know how many arguments will be passed, add a `*` before the parameter name. This allows the function to receive a **tuple** of arguments.

```python
def my_function(*kids):
  # Access item using index
  print("The youngest child is " + kids[2]) 
  return kids

kids_names = my_function("Emil", "Tobias", "Linus")

```

### 4. Memory and Pointers in Python (`PengenalanPointer.py`)

Unlike C++, Python handles memory management automatically. You generally don't use "pointers" manually, but variables are actually references to objects in memory. We can see the memory address using `id()`.

```python
import sys

a = 10
ptr = a # 'ptr' references the same object as 'a'

# Check Memory Address (ID)
print(f"Alamat dari a (id): {id(a)}")

# Check Size in Memory
print(f"Ukuran dari nilai a adalah {sys.getsizeof(a)}")

```

---

## Part 2: Classes and Objects (OOP)

Python is an Object-Oriented language. Classes act as blueprints for creating objects.

### 5. Creating a Class (`Class.py` & `Pass.py`)

Use the `class` keyword to define a blueprint. If a class is empty, use `pass` to avoid errors.

```python
class MyClass:
  x = 5

p1 = MyClass() # Create Object
print(p1.x)    # Access Property

```

### 6. The `__init__` Constructor (`Init.py` & `Class2.py`)

The `__init__()` function is automatically called when you create a new object. It is used to initialize the object's initial values.

```python
class Mahasiswa:
    def __init__(self, nama, nrp, umur):
        self.nama = nama
        self.nrp = nrp
        self.umur = umur

mhs1 = Mahasiswa("Ahmad", "05111940000012", 18)
print(f"Nama: {mhs1.nama}")

```

### 7. Object Methods (`ObjectMethod.py` & `SelfParameter.py`)

Objects can contain functions (methods). The `self` parameter allows these methods to access and modify the specific object's attributes.

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

```

### 8. String Representation (`str.py`)

The `__str__()` method controls what is shown when you try to print the entire object.

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1) # Output: John(36)

```
