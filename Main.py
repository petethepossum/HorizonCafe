import time
debug = bool(True)
#hasSugar = any

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
sugarArray=[] #This isn't needed can append sugar info to order info as a whole
#Might need to store total order price differently??
orderArray =[] 

def namefunction():
    name = input('Enter your name for the order ')
    nameArray.append(str("Name:")) #THIS IS MESSY but helps demonstrate fstrings
    nameArray.append(str(name))
    
    print (name) #15/3 made it print the string not the array data giving a cleaner output
    time.sleep(1)
namefunction()

#Could I make the function repeat itself based on an amount of coffees wanted?? - ASK MISS UTTING MAYBE A FOR LOOP????
def orderfunction(): #THIS FIX WORKS! Before hand the coffee variable was not handled properly in the function, when selected it would automatically select the last item in the menu, to fix this I gave selected coffee its own variable, in hindsight I shoudlv'e done this much sooner.
    for option, coffee in menu.items():
        print(f"{option}. {coffee['type']} | ${coffee['cost']}")
    coffeeInfo = input("Please enter the number of the Coffee you would like to order ")
    if coffeeInfo not in menu:
        print("This is not a listed coffee please try again")
        time.sleep(1)
        orderfunction()
    else:
        selected_coffee = menu[coffeeInfo]["type"]
        orderArray.append(menu[coffeeInfo])
        def withSugarprint():
            print("Your order is: " + str(nameArray[1]) + " " + str(selected_coffee) + " with " + str(sugarArray) + " sugar")
        def noSugarprint():
            print("Your order is: " + str(nameArray[1]) + " " + str(selected_coffee) + " with no sugar") 
        def sugarfunction():
            Sugar = float(input('How many servings of sugar would you like in your coffee? (number between 0-10) ')) #Floating point numbers for example 1.5 sugar DO work have tested
            if Sugar == 0:
                print("No sugar added")
                noSugarprint()
            else:
                sugarArray.append(float(Sugar)) 
                orderArray.append(sugarArray) 
                withSugarprint()
        sugarfunction()
        
orderfunction()    
print(orderArray)

#Handle this before we show the menu as we can run order select twice
def miscfunction():
    time.sleep(2)
    print("Print both arrays to check stored value ") #Need to make this relate to the debug var
    print(nameArray)
    print(orderArray)
if debug == (True):
    miscfunction()



