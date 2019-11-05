#Accept string from the user and display only those characters which are present at an even index

#My Solution
word = input("Enter String")
print("Original String is " + word)
print("Printing only even index chars")
for idx, char in enumerate(word):
  if idx % 2 == 0:
    print("index[ " + str(idx) + " ] " + char)
    
#Given Solution
def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = input("Enter String ")
print("Orginal String is ", inputStr)

print("Printing only even index chars")
printEveIndexChar(inputStr)
