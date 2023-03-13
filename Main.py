import time

#First thing to do is list coffe types and print them

#Im going to use a single array list of friendly names here as it might make defining prices easier later on we will see I might be wrong
cf1=['FlatWhite']
cf2=['Cappuchino']
cf3=['Latte']
cf4=['Decaf']
cf5=['Hot Chocolate']

#Define arrays for storing use data such as name
nameArray=[]
ammountArray=[]

name = input('enter your name for the order')
nameArray.append(str(name))
print (nameArray)
time.sleep(1)
ammount = input('how many coffees would you like?')
ammountArray.append(str(ammount))
print(ammount)