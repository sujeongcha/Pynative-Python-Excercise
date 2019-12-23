#Given two sets, Checks if One Set is Subset or superset of Another Set. if the subset is found delete all elements from that set

#My Solution
set1 = {57, 83, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}

print("First Set ", set1)
print("Second Set ", set2)

print("\nFirst set is subset of second set - ", set1.issubset(set2))
print("Second set is subset of First set - ", set2.issubset(set1))

print("\nFirst set is Super set of second set - ", set1.issuperset(set2))
print("Second set is Super set of First set - ", set2.issuperset(set1))

set1.clear()
print("\nFirst Set ", set1)
print("Second Set ", set2)

#Given Solution
firstSet  = {57, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", firstSet)
print("Second Set ", secondSet)

print("First set is subset of second set -", firstSet.issubset(secondSet))
print("Second set is subset of First set - ", secondSet.issubset(firstSet))

print("First set is Super set of second set - ", firstSet.issuperset(secondSet))
print("Second set is Super set of First set - ", secondSet.issuperset(firstSet))

if(firstSet.issubset(secondSet)):
  firstSet.clear()
  
if(secondSet.issubset(firstSet)):
  secondSet.clear()

print("First Set ", firstSet)
print("Second Set ", secondSet)
