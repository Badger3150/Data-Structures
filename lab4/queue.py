# Q2 - Queue
import queue
import re

sequence = queue.Queue()

def getNum(string):
    Info = re.findall(r"\d+", transaction)
    return([int(Info[0]), int(Info[1])])

transaction = input("What's your transaction? ")
while transaction[:3] == "buy":
    sequence.put(getNum(transaction))
    transaction = input("What's your transaction? ")

if transaction[:4] == "sell":
    sum = 0
    sellInfo = getNum(transaction)
    sellPrice = sellInfo[1]
    while not sequence.empty():
        buyInfo = sequence.get()
        sum += (sellPrice - buyInfo[1]) * buyInfo[0]
    print("The capital gain is: $", sum)
else:
    print('Wrong input')

