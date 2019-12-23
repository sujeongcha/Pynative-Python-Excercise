#Remove duplicate from a list and create a tuple and find the minimum and maximum number

#My Solution
sampleList = [87, 52, 44, 53, 54, 87, 52, 53]

uniqueList = []
for num in sampleList:
  if num not in uniqueList:
    uniqueList.append(num)

print("unique items ", uniqueList)
print("tuple ", tuple(uniqueList))
print("min: ", min(uniqueList))
print("max: ", max(uniqueList))

#Given Solution
sampleList = [87, 52, 44, 53, 54, 87, 52, 53]

print("Original list", sampleList)

sampleList = list(set(sampleList))
print("unique list", sampleList)

tuple = tuple(sampleList)
print("tuple ", tuple)

print("Minimum number is: ", min(tuple))
print("Maximum number is: ", max(tuple))
