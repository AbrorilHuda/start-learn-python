myList = ["aku","kamu","kita"]
# bisa di isi string boolean int
print(myList)

#menghitung list
print(len(myList))

# menggunaka func list()
myListTwo = list(("aku","mencitain","mu")) #penulisan double round-brackets()

print(myListTwo)



# acces items ini seperti array kalok di bahasa pemograman yang lain
print(myList[0]) # aku
print(myList[-1]) # kita
print(myList[1:2]) # kamu

# update || chage data from list
myList[0] = "iam" # aku > iam
print(myList)

# add list
myList.append("testing")
print(myList)
myList.insert(0,"hahaha")
print(myList)
# menghabungkan 2 list
myList.extend(myListTwo)
print(myList)

# remove list
myList.remove("hahaha")
print(myList)

# specified index
myList.pop(0)
print(myList)


# menggunakan keyword del
del myList[0]
print(myList)


#clear list content
myList.clear()
print(myList)




# perulangan di list

for x in myListTwo:
    print(x)

print("ini di looping menggunakan index number")
# looping index number
for i in range(len(myListTwo)):
    print(myListTwo[i])

print("meggunakan while")

#while
a = 0
while a < len(myListTwo):
    print(myListTwo[a])
    a = a + 1


# comprehension
[print(x) for x in myListTwo]

fruits = ["apple", "Banana", "cherry", "kiwi", "mango"]
numerikal = [23,41,54,100,4,25,2,1,5]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)

# versi comprehension
newlist = [x for x in fruits if "a" in x]
print(newlist)


#sort

fruits.sort()
print(fruits)

numerikal.sort()
print(numerikal)

# descending
numerikal.sort(reverse=True)
print(numerikal)


#reverse
fruits.reverse()
print(fruits)
