mydiction = {
    "name": "abrordc",
    "street": "jln jln",
    "year": 2025
}
print(mydiction)


# print one item
print(mydiction["name"])

# data not duplicate
# examplediction = {
#     "name": "abrordc",
#     "name": "abro"
# }

# untuk menghitung data
print(len(mydiction))


# untuk data bebas untuk di isi
dataDummy = {
    "name": "abrordc",
    "year": 2025,
    "hobbies": ["coding","ngoding","ngode"]
}

print(dataDummy)
print(dataDummy["hobbies"][0]) # untuk mencetak data di dalam list


# bisa juga membuatnya dengan func dict()
dataDict = dict(name="people", one="someone")
print(dataDict)


# acces item for dict

#key
print(dataDummy.keys()) # mencetak semua key dict

#get
print(dataDummy.get("year")) # mengambil data sesuai key

#values
print(dataDummy.values()) # mengamil semua data tanpa key

#items
print(dataDummy.items()) # mengeloppok kan sesuai dengan keynya


#add data
dataDummy["languange"] = "javascripts"
print(dataDummy)

#change data
dataDummy["year"] = 2018
print(dataDummy)

#update
dataDummy.update({"name" : "abrormdrd"})
print(dataDummy)


# remove data
#pop
dataDummy.pop("year")
print(dataDummy)

#popitem remove last data
# dataDummy.popitem()
# print(dataDummy)

#clear data
# dataDummy.clear()
# print(dataDummy)

# perulangan data
#print key data
for x in dataDummy:
    print(x)

# print data
for i in dataDummy:
    print(dataDummy[i])


#values
for a in dataDummy.values():
    print(a)

#keys
for k in dataDummy.keys():
    print(k)


#items
for key,value in dataDummy.items():
    print(key, value)



#nested dict
dataDummyNested = {
    'child1': {
        "name": "po",
        "no": 1
    },
    'child2': {
        "name": "lam",
        "no": 2
    }
}

print(dataDummyNested["child1"]["name"]) # child1 > name "po"

for data, obj in dataDummyNested.items():
  print(data,"=>")
  for y in obj:
    print(y + ':', obj[y])

