import random

def randomNumPair():
    while True:
        num = random.randrange(0,100)
        if num % 2 == 0:
            return num
        continue

def randomOddNumber():
    while True:
        num = random.randrange(0,100)
        if num % 2 != 0:
            return num
        continue
               

print(randomOddNumber())