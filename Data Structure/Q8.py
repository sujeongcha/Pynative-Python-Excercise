#Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list

#My Solution
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

newList = []
for num in rollNumber:
  if num in sampleDict.values():
    newList.append(num)

print("after removing unwanted elements from list ", newList)

#Given Solution
rollNumber  = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict  ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97} 

print("List -", rollNumber)
print("Dictionary - ", sampleDict)

rollNumber[:] = [item for item in rollNumber if item in sampleDict.values()]
print("after removing unwanted elemnts from list ", rollNumber)
