mytuple = ("hai","aku","kamu","aku","kamu")
print(mytuple)


# menghitug data tuple

print(len(mytuple))

# cek type
print(type(("people",)))

#not a tuple
print(type(("people")))


# mebuat tuple dengan func tuple()
myTupleTwo = tuple(("some","one"))
print(myTupleTwo)


#acces tuple
print(mytuple[0])

# update

datadame = list(myTupleTwo)
datadame[0] = "mencintai"
myTupleTwo = tuple(datadame)
print(myTupleTwo)

# tuple + tuple
sementara = ("menjauh",)
myTupleTwo += sementara
print(myTupleTwo)

#remove
datadame.remove("mencintai")
myTupleTwo = tuple(datadame)
print(myTupleTwo)



# unpacking tuple

unpack = ("aku","mencintaimu")

iam,healt = unpack
print(iam)
print(healt)

# asterik kalok di js namanya distruccering
unpackTwo = ("aku","mencintaimu","namun","....")
im,des,*gel = unpackTwo
print(im)
print(des)
print(gel)

# perulangan di tuple
for x in unpackTwo:
    print(x)

# index numeric
for i in range(len(unpackTwo)):
    print(unpackTwo[i])



#while
a = 0
while a < len(unpackTwo):
    print(unpackTwo[a])
    a = a + 1
