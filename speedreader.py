from time import sleep
from os import system
import sys

j=input(">")
while True:
    system("cls")
    inp=sys.stdin.read()
    system("cls")
    inp=inp.strip()
    words=inp.split()
    bar,lgth='',len(words)
    for c,i in enumerate(words):
        bar=int(100*(c/lgth))
        print(u' '*34+u'['+u'█'*bar+(100-bar)*u' '+u']')
        print("\n"*18+" "*(85-len(i)//2)+i)
        if len(i)<6:
            sleep(float(j))
        else:
            sleep(float(j)+.06)
        system("cls")
    system("pause")