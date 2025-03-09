# while

i = 0
while i < 6:
    print(i)
    i = i + 1

r = 0
while r < 6:
    if r == 4:
        break
    print("=" * r)
    r = r + 1

c = 0
while c < 6:
    print("saya mengulang sekitar", c)
    c = c + 1
else:
    print("sudah lebih dari 6 guys gak boleh")


e = 0
while e < 6:
  e += 1
  if e == 3:
    continue
  print(e)


# for

fordata = ["name","is","abrordc"]

for x in fordata:
    print(x)

for v in "abrordc":
    print(v)

for b in fordata:
    if "is" in b: break
    print(b)

dataDict = {
    "name": "anjas",
    "level": 78,
    "skins": ["legends","epic","elite"]
}

for key,obj in dataDict.items():
    print(key, obj)
    if type(obj) == type(list()):
        for l in dataDict["skins"]:
            print(l)