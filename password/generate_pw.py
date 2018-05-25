import string
import random
import sys

def generate(length):
    num3 = string.printable
    print (num3)
    return ''.join(random.choice(num3) for _ in range(length))
    

print (generate(int(sys.argv[1])))
