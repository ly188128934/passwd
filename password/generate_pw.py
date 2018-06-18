import string
import random
import sys


def generate(length,*pw_type):
    all_pw = ''
    for num in pw_type:
        print num
        num1 = str(num)
        return string.(str(um1))
        #all_pw += string.(str(num))
        #print all_pw
    return ''.join(random.choice(all_pw) for _ in range(length))

#length,digits,letters,lowercase,printable,punctuation,uppercase

print (generate(int(sys.argv[1]),'digits','letters','lowercase','punctuation','uppercase'))
