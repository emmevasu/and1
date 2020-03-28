from faker import *
from random import *
n=int(input("enter student length:"))
for i in range(n):
    fakers=Faker()
    sid=randint(100000,500000)
    sname=fakers.name()
    smarks=randint(1,101)
    print('sid:',sid)
    print('sname:',sname)
    print('smarks:',smarks)
    
