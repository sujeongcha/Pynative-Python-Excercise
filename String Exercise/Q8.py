#Print the following pattern

#My Solution
for i in range(5):
  word = str(i+1) + " "
  print(word*(i+1)) 
  
#Given Solution
for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
