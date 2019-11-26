#arrange String characters such that lowercase letters should come first

#My Solution
def lowerFirst(s1):
  lower = ""
  upper = ""
  for a in s1:
    if a.islower():
      lower += a
    else:
      upper += a
  print("input_String =", s1)
  print("arranging characters giving precedence to lower case letters:")
  print(lower+upper)
  
lowerFirst("PyNaTive")

#Given Solution * ''.join(list1+list2)
inputStr = "PyNaTive"
words = inputStr.split()
lower = []
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = ''.join(lower + upper)
print("\n arranging characters giving precedence to lowercase letters:")
print(sortedString)
