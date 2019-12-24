#Random Lottery Pick

#My Solution
import random

lotteryList = []
while len(lotteryList) < 100:
  lot = random.randrange(1000000000, 9999999999)
  if lot not in lotteryList:
    lotteryList.append(lot)

print("Lucky 2 lottery tickets are ", random.sample(lotteryList, 2))

#Given Solution
import random

lottery_tickets_list = []
print("creating 100 random lottery tickets")
for i in range(100):
    lottery_tickets_list.append(random.randrange(1000000000, 9999999999))

winners = random.sample(lottery_tickets_list, 2)
print("Lucky 2 lottery tickets are", winners)
