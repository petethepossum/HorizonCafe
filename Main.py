import time
debug = bool(False)

#First thing to do is list coffe types and print them

#Im going to use a single array list of friendly names here as it might make defining prices easier later on we will see I might be wrong
cf1=['FlatWhite']
cf2=['Cappuchino']
cf3=['Latte']
cf4=['Decaf']
cf5=['Hot Chocolate']
#Don't think this is needed anymore not sure reading up on list, might change to a dictionary so can contain values etc

menu = {
   "1": {"type": "Flat White", "cost": 3.00},
   "2": {"type": "Cappuccino", "cost": 3.00},
   "3": {"type": "Latte", "cost": 3.50},
   "4": {"type": "Decaf", "cost": 3.00},
   "5": {"type": "Hot Chocolate", "cost": 4.00}
}

#Define arrays for storing use data such as name
nameArray=[] #This still might be useful to store seperatly
ammountArray=[] #This isn't needed can append ammount info to order info as a whole
sugarArray=[] #This isn't needed can append sugar info to order info as a whole
#Might need to store total order price differently??
order =[] 

def namefunction():
    name = input('Enter your name for the order ')
    nameArray.append(str(name))
    print (name) #15/3 made it print the string not the array data giving a cleaner output
    time.sleep(1)
namefunction()


def orderfunction(): #15/3 changed to order function as will nest the ordering process within this function SOON™
    for option, coffee in menu.items():
        #Useing F-String ticks of an "advanced feature" on the work sheet
        print(f"{option}. {coffee['type']} | ${coffee['cost']}")
    #NEED TO HANDLE ORDER SELECTION IN HERE
    coffeeInfo = input("Please enter the number of the Coffee you would like to order ")
    if coffeeInfo != menu.items:
        print("This is not a listed coffee please try again")
        time.sleep(3)
        exit()


    order.append({}) #How do I do this?
orderfunction()    



ammount = input('how many coffees would you like? ')
ammountArray.append(str(ammount))
print(ammount)
time.sleep(2)
print("Print both arrays to check stored value ") #Need to make this relate to the debug var
print(nameArray)
print(ammountArray)


#Sugar Input function (How can I change this to be better) should have it in the order selection function as an if statement?
def sugarfunction():
    Sugar = (input('How many servings of sugar would you like in your drink? (Please enter a number) '))
    sugarArray.append(int(Sugar))
    print(sugarArray)
    #Calls function??
sugarfunction()


