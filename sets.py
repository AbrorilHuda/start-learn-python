myset = {"i","love","you"}
print(myset)

#duplicate not allowed
mySetDouble = {"iam","iam","love","it"}

print(mySetDouble) #{"love","iam","it"}


checked = {"data",False,True,0}
print(checked) # nul not print or 1 is print

#menghitung data sets
print(len(myset))


# membuat set menggunak func set()
dataDummyFunc = set(("love","me"))
print(dataDummyFunc)


# cek data menggunakan in
print("love" in dataDummyFunc) # jika tidak ada False
print("love" not in dataDummyFunc) #jika data ada false



# Add item for data sets && add set
dataDummyFunc.add("and")
print(dataDummyFunc)

#example add set for data set
addSetsDummy = {"you","and","me","together"}
dataDummyFunc.update(addSetsDummy)
print(dataDummyFunc)

#example add update data from list
dataListDummy = ["my","love"]
dataDummyFunc.update(dataListDummy)
print(dataDummyFunc)


# delete data from sets
dataDummyFunc.remove("love")
print("love di hapus",dataDummyFunc)

#use discard
dataDummyFunc.discard("me")
print("me di hapus", dataDummyFunc)

# random remove
randomRemove = dataDummyFunc.pop()
print(randomRemove)

print("setelah di hapus random: ",dataDummyFunc)

# membersihkan
dataDummyFunc.clear()
print(dataDummyFunc)

#bisa juga sih pakek del keyword



# perulangan data set
for x in mySetDouble:
    print(x)

# join
grupData = myset.union(mySetDouble)
grupDataDua = myset | mySetDouble

print(grupData)
print(grupDataDua)