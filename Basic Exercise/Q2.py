#Question 2: Given a range of numbers. 
#Iterate from o^th number to the end number and print the sum of the current number and previous number

#My Solution
def cur_pre_sum(nums):
  for i in range(len(nums)):
    if i == 0:
      print(nums[i])
    else:
      print(nums[i] + nums[i-1])
      
print("Printing current and previous number sum in a given range")
cur_pre_sum([0,1,2,3,4,5,6,7,8,9])

#Best Solution
def sumNum(num):
  previousNum=0
  for i in range(num):
    sum = previousNum + i
    print(sum)
    previousNum = i   **re-setting the previous number

print("Printing current and previous number sum in a given range")
sumNum(10)
