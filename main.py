from random import choice
from string import ascii_letters
import hashlib
from threading import Thread


def miner():
    while True:
        test_string = '167298936-'+"".join([choice(ascii_letters) for _ in range(10)])
        if hashlib.md5(test_string.encode('utf8')).hexdigest().startswith('000000'):
            with open('data.txt', 'a') as file:
                file.write(test_string)
                print(test_string)

for i in range(30):
    Thread(target=miner).start()