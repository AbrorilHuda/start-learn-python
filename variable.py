satu = 1
dua = 2


# camelCase
namaSaya = "abrordc"

#PascalCase
IniSaya = "AbrorDc"

#snake-case
my_name = "abror-dc"

# one line many Values
a,b,c = "nanas", "anggur","piton"


#global variable nanti kita ada file pembahasan fungsi kita bahas global variable

# x sebagai global variable
x = "global"

def myFunc():
    x = "di isi di scope function"
    print("this is scope func :",x)

myFunc()
print(x)

# atau menggunak keyword global

def iniFunc():
    global  y
    y = "ini example global keyword"

iniFunc() # ini tidak mencetak apa2
print("example global keyword:", y)



print(f"ini variable a: {a}, ini variable b: {b}, ini variable c: {c}")
print("ini camelCase: ",namaSaya)
print("ini PascalCase: ", IniSaya)
print("ini snake-case: ", my_name)
print("hasil dari 1 + 2: ", satu + dua)


