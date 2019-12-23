#Given a list slice it into a 3 equal chunks and rever each list

#My Solution
def threeChunk(numList):
  cut = len(numList) // 3
  chunkOne = numList[:cut]
  chunkTwo = numList[cut:cut*2]
  chunkThree = numList[cut*2:]
  print("Original list ", numList)
  print("Chunk 1 ", chunkOne)
  print("After reversing it ", chunkOne[::-1])
  print("Chunk 2 ", chunkTwo)
  print("After reversing it ", chunkTwo[::-1])
  print("Chunk 3 ", chunkThree)
  print("After reversing it ", chunkThree[::-1])

threeChunk([11, 45, 8, 23, 14, 12, 78, 45, 89])

#Given Solution
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sampleList)

length = len(sampleList)
chunkSize  = int(length/3)
start = 0
end = chunkSize
for i in range(1, 4, 1):
  indexes = slice(start, end, 1)
  listChunk = sampleList[indexes]
  print("Chunk ", i , listChunk)
  print("After reversing it ", list(reversed(listChunk)))
  start = end
  if(i != 2):
    end +=chunkSize
  else:
    end += length - chunkSize
