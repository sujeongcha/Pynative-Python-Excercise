#Given a string and an int n, remove characters from string starting from zero up to n and return a new string

#My Solution
def removeChars(word, n):
  result = word[n:]
  print("Removing n number of chars")
  print(result)
  
removeChars("pynative", 4)

#Given Solution
def removeChars(str, n):
  return str[n:]

print("Removing n number of chars")
print(removeChars("pynative", 4))
