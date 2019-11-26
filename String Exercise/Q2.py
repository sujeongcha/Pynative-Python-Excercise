#Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1

#My Solution
def appendMiddle(s1, s2):
  i = int(len(s1) / 2)
  print("Original Strings are", s1, s2)
  print("After appending new string in the middle", s1[0:i] + s2 + s1[i:])
  
appendMiddle("Chrisdem", "IamNewString")

#Best Solution
def appendMiddle(s1, s2):
  middleIndex = int(len(s1) /2)
  print("Original Strings are", s1, s2)
  middleThree = s1[:middleIndex-1:]+ s2 +s1[middleIndex-1:]
  print("After appending new string in middle", middleThree)
  
appendMiddle("Chrisdem", "IamNewString")
