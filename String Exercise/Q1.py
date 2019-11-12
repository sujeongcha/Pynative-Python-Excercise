#Given a string of odd length greater 7, return a string made of the middle three chars of a given String

#My Solution
def getMiddleThreeChars(word):
  mid = len(word) // 2
  print("Original String is ", word)
  print("Middle three chars are ", word[mid-1:mid+2])
  
getMiddleThreeChars("JhonDipPeta")
getMiddleThreeChars("Jasonay")

#Given Solution
def getMiddleThreeChars(sampleStr):
  middleIndex = int(len(sampleStr) /2)
  print("Original String is", sampleStr)
  middleThree = sampleStr[middleIndex-1:middleIndex+2]
  print("Middle three chars are", middleThree)
  
getMiddleThreeChars("JhonDipPeta")
getMiddleThreeChars("Jasonay")
