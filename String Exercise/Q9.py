#Reverse a given number and return true if it is the same as the original number

#My Solution
def reverseNum(num):
  newnum = int(str(num)[::-1])
  return num == newnum
  
number = 121
print("Original and reverse number is equal")
print(reverseNum(number))
    
#Given Solution
def reverseCheck(number):
  originalNum = number
  reverseNum=0
  while(number > 0):
    reminder = number % 10
    reverseNum  = (reverseNum *10) + reminder
    number = number // 10
  if(originalNum  == reverseNum):
    return True
  else:
    return False
    
print("orignal and revers number is equal")
print(reverseCheck(121))
