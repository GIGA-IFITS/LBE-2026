def math(a, b):
    c = a + b
    print("Hasil pertambahannya adalah", (c))

# Ask user to input 2 integers
a, b = map(int, input("Masukkan 2 angka yang ingin ditambahkan (pisahkan dengan spasi): ").split())

# Same result using: 
# a = int(input("Masukan a: "))
# b = int(input("Masukan b: "))

math(a, b)