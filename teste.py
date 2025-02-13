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

def test_pair():
    assert randomNumPair() % 2 == 0
def test_odd():
    assert randomOddNumber() % 2 != 0

print(randomOddNumber())