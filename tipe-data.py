angka = 1 #int
bulat = 1.2 #float
campur = 1j #complex


name = "abrordc" #string
description = '''
aku padamu horeg interage
dashmoe
''' # multipleline


print(type(angka))
print(type(bulat))
print(type(campur))
print(type(name))
print(type(description))




print("="*30)
print("convert type data :")

datainterger = 1
datafloat = 2.2
datacomplex = 1j

#prosess convert
integertofloat = float(datainterger)
print("integer to float :", integertofloat)

floattointeger = int(datafloat)
print("float to integer :", floattointeger)

intergertocomplex = complex(datainterger)
print("integert to complex :", intergertocomplex)


print("="*30)
print("hal hal prosess cheasheet di type string")

# mengambil karakter
print(name[1])  # b

#looping string
for x in name:
    print(x)

# menghitung semua karakter
print(len(name))

#check string
print("dc" in name) # boolean




