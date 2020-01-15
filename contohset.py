buah1 = {"apple","orange","durian"}
buah2 = {"durian","rambutan"}

buah = buah1.union(buah2)
buahall = list(buah1)+list(buah2)
buahinter = buah1.intersection(buah2)
buahdiff = buah1.difference(buah2)

print(buah)
print(buahall)
print(buahinter)
print(buahdiff)