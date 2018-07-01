import string
import random
import sys
import re

#生成密码，放在本地执行，生成后上传到服务器

def generate(length,pw_type):
    if pw_type == '0':
        return ''.join(random.choice(string.digits) for _ in range(length))
    elif pw_type == '1':
        return ''.join(random.choice(string.digits+string.letters) for _ in range(length))
    elif pw_type == '2':
        #return (string.printable).replace('\\','').replace('|','').replace('%','')
        return ''.join(random.choice((string.printable).replace('_','').replace('\\','').replace('?','').replace('`','').replace('|','').replace().replace('\"','').replace('~','').replace('\'','').replace('<','').replace('>','')) for _ in range(length))

print (str(generate(int(sys.argv[1]), sys.argv[2])))