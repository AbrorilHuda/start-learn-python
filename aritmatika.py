print("operasi matematika")


print(1 + 2) #additin
print(2 - 1) #subtraction
print(2 * 2) #multiplication
print(3 / 2) #devision
print(3 % 4) #modulus
print(2 ** 2) #exponentiation
print(2 // 2) #floor devision

print("="*30)
print("Assigment Operator")
# Assignment Operator
x = 5
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x //= 3
print(x)
x **= 3
print(x)
#x &= 3 # and biner
#print(x)
#x |= 3
#print(x)
#x ^= 3
#print(x)
#x >>= 3
#print(x)
#x <<= 3
#print(x)
print(y := 3)


print("="*30)
print("Comparison Operators")
# opeartor perbandingan
kecil = 1
besar = 10
print(kecil == besar)
print(kecil != besar)
print(kecil > besar)
print(kecil < besar)
print(kecil >= besar)
print(kecil <= besar)

# Logical Operators
print("="*20)
# and keduanya harus benar
# or salah satunya harus benar

print(kecil > besar and besar > kecil) # false and true = false
print(kecil > besar or besar > kecil) # false or true = true
print(not(kecil < besar)) # jika salah true jika benar false

#bembandingkan objek yang sama dengan lokasi memory yang sama
print(kecil is besar)
print(kecil is not besar)