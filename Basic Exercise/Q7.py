#Return the number of times that the string “Emma” appears anywhere in the given string

#My Solution
def EmmaCount(word):
  counter = 0
  for i in range(len(word)):
    if word[i:i+4] == "Emma":
      counter += 1
  return counter

print("Emma appeared " 
      + str(EmmaCount("Emma is a good developer. Emma is also a writer")) 
      + " times")
      
#Given Solution
def count_jhon(statement):
  count = 0
  for i in range(len(statement)-1):
    count += statement[i:i+4] == 'Emma'
  return count

count = count_jhon("Emma is good developer. Emma is aslo a writer")
print("Emma appeared ", count, "times")
