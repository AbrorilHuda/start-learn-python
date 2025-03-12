# function
def my_func():
     print("my function")
# memanggil func
my_func()

# function anda argument
def cetak(data):
    print(data)


cetak("hello world")

def Noarbitari(data1,data2,data3):
    print(data1,data2,data3)

Noarbitari("data1","data2","data3")
# arbitari arguemnt
def Arbitari(*args):
    print(args)

Arbitari("hello", "world","semua")


# arbitari keyword
def keywordData(**kwargs):
    print(kwargs)

keywordData(name="sulaimna",date="rabu-kamis")



"""lambda func"""

func = lambda a:a + 2


#pangkat exemple

def pangkat(n):
    return lambda a:a ** n

number = pangkat(4)

print(number(3))