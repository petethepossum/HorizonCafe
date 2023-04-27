import time
debug = bool(False)
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
ammountArray=[] #This isn't needed can append ammount info to order info as a whole?? Maybe a for loop idk
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
def orderfunction(): #15/3 changed to order function as will nest the ordering process within this function SOON™
    for option, coffee in menu.items():
        #Using F-String ticks of an "advanced feature" on the work sheet
        print(f"{option}. {coffee['type']} | ${coffee['cost']}")
    #NEED TO HANDLE ORDER SELECTION IN HERE
    coffeeInfo = input("Please enter the number of the Coffee you would like to order ")
    if coffeeInfo not in menu:
        print("This is not a listed coffee please try again")
        time.sleep(1)
        orderfunction()
        #exit() #Need to make this return
        #orderfunction()
    else:
        def withSugarprint(): #There's probably a better way to do this but it works
            print("Your order is: " + str(nameArray[1]) + " " + str(coffee['type']) + " with " + str(sugarArray) + " sugar") 
        def noSugarprint():
            print("Your order is: " + str(nameArray[1]) + " " + str(coffee['type']) + " with no sugar") 
        def sugarfunction():
            Sugar = float(input('How many servings of sugar would you like in your coffee? (number between 0-10) ')) #Its saved as a float so should handle decimals okay
            if Sugar == 0:
                print("No sugar added")
                noSugarprint()
                #set: hasSugar = False
            else:
                #sugarArray.append(str("Sugar:")) #Surely there is a better way to add this to the array?
                sugarArray.append(float(Sugar))
                #print(sugarArray)
                orderArray.append(sugarArray) 
                withSugarprint()

                #set: hasSugar = True
    
        print("ok debug man")
        #print(coffee['type'])
        orderArray.append(nameArray)
        orderArray.append(coffee['type'])
        sugarfunction()
orderfunction()    


#Handle this before we show the menu as we can run order select twice
def miscfunction():
    ammount = input('how many coffees would you like? ')
    ammountArray.append(str(ammount))
    print(ammount)
    time.sleep(2)
    print("Print both arrays to check stored value ") #Need to make this relate to the debug var
    print(nameArray)
    print(ammountArray)
if debug == (True):
    miscfunction()



