import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "{}[]#@;<>._-\/"


all=lower + upper + number + symbol
length = 15
password = "".join(random.sample(all,length))
print (''
'')
print(" Password Generator by 0xSatan")
print(''
'')
print(" The Password You Generated is :",password)
print(''
'')
print(" Generator Coded/Made By 0xSatan")
print (''
'') 
