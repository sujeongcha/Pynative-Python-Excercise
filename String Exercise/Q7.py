#Return the number of times that the string “Emma” appears anywhere in the given string

#My Solution
def wordCount(str):
  count = 0
  for idx in range(len(str)):
    if str[idx:idx+4] == "Emma":
      count += 1
  return count

result = wordCount("Emma is good developer. Emma is aslo a writer")
print("Emma appeared", result, "times")    

#Given Solution
def count_jhon(statement):
  count = 0
  for i in range(len(statement)-1):
    count += statement[i:i+4] == 'Emma'
  return count

count = count_jhon("Emma is good developer. Emma is aslo a writer")
print("Emma appeared ", count, "times")
