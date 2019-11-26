#Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string

#My Solution
def mixString(s1, s2):
  s1idx = int(len(s1)/2)
  s2idx = int(len(s2)/2)
  print(s1[0]+s2[0]+s1[s1idx]+s2[s2idx]+s1[-1]+s2[-1])
  
mixString("America", "Japan")

#Given Solution
def mixString(s1, s2):
  resultString = s1[:1] + s2[:1] + s1[int(len(s1) /2):int(len(s1) /2)+1] +s2[int(len(s2) /2):int(len(s2) /2)+1] +s1[len(s1)-1] + s2[len(s2)-1]
  print("Mix String is ", resultString)
  
s1 = "America"
s2 = "Japan"
mixString(s1, s2)
