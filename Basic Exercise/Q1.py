#Question 1: Accept two int values from the user and return their product. 
#If the product is greater than 1000, then return their sum.

#My Solution
first = int(input("Enter first number "))
second = int(input("Enter second number "))

product = first*second
sum = first+second

if product > 1000:
  print("The result is ", sum)
else:
  print("The result is ", product)
  
#Best Solution
def multiplication_or_sum(num1, num2):
  product = num1 *num2
  if(product < 1000):
    return product
  else:
    return num1 +num2

number1 = int(input("Enter first number "))
number2 = int(input("Enter second number "))

result = multiplication_or_sum(number1, number2)
print("The result is", result)
