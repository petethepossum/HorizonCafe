import time
debug = bool(False)

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
sugarArray=[]

def namefunction():
    name = input('enter your name for the order ')
    nameArray.append(str(name))
    print (nameArray)
    time.sleep(1)
namefunction()


#Need to do print coffe type and price 

ammount = input('how many coffees would you like? ')
ammountArray.append(str(ammount))
print(ammount)
time.sleep(2)
print("Print both arrays to check stored value ")
print(nameArray)
print(ammountArray)


#Sugar Input function
def sugarfunction():
    Sugar = (input('How many servings of sugar would you like in your drink? (Please enter a number) '))
    sugarArray.append(int(Sugar))
    print(sugarArray)
    #Calls function
    sugarfunction()


