#Given a following two sets find the intersection and remove those elements from the first set

#My Solution
set1 = {65, 42, 78, 83, 23, 57, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}
intersection = set1.intersection(set2)
set1.difference_update(intersection)

print("First Set ", set1)
print("Second Set ", set2)
print("Intersection is ", intersection)
print("First Set after removing common element", set1)

#Given Solution
firstSet  = {23, 42, 65, 57, 78, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", firstSet)
print("Second Set ", secondSet)

intersection = firstSet.intersection(secondSet)
print("Intersection is ", intersection)
for item in intersection:
  firstSet.remove(item)

print("First Set after removing common element ", firstSet)
