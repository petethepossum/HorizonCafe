import time
debug = bool(False)

#First thing to do is list coffe types and print them

#Im going to use a single array list of friendly names here as it might make defining prices easier later on we will see I might be wrong
cf1=['FlatWhite']
cf2=['Cappuchino']
cf3=['Latte']
cf4=['Decaf']
cf5=['Hot Chocolate']
#Don't think this is needed anymore not sure reading up on list

#Define arrays for storing use data such as name
nameArray=[]
ammountArray=[]
sugarArray=[]
orderArray=[]

def namefunction():
    name = input('Enter your name for the order ')
    nameArray.append(str(name))
    print (nameArray)
    time.sleep(1)
namefunction()


def menufunction():
    print("---Horizon Cafe Menu---")
    print("1. Flat White | $3.00\n2. Cappuccino | $3.00\n3. Latte | $3.50\n4. Decaf Coffee | $3.00\n5. Hot Chocolate | $4.00")
menufunction()    


ammount = input('how many coffees would you like? ')
ammountArray.append(str(ammount))
print(ammount)
time.sleep(2)
print("Print both arrays to check stored value ") #Need to make this relate to the debug var
print(nameArray)
print(ammountArray)


#Sugar Input function (How can I change this to be better)
def sugarfunction():
    Sugar = (input('How many servings of sugar would you like in your drink? (Please enter a number) '))
    sugarArray.append(int(Sugar))
    print(sugarArray)
    #Calls function??
sugarfunction()


