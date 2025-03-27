#Let's build a robot barrista using variables in Python
#print ("Hello Welcome to NetworkChuck coffee!!!")
#input ("What is your name?")

print ("Hello! Welcome to GoogleDeepmind Coffee")

print ("My name is Edouard")

name = input( "What is your name?\n " )

menu = "Latte, Cappucino, Espresso, Mocha, Tea"

# Here we used an if else statement to prevent 

if name == "Ben":
   print ("You are not welcome here Evil Ben! Go before we call the authorities")
   exit() 
else: 
    print( "Hello " + name + ", What would you like to order from the menu today? Here is what we are serving. \n" + menu )


order = input ()

#Now we are going to use elif to set the price for each cup of coffee 

if order == "Latte":
    price = 3 
elif order == "Cappucino": 
    price = 5 
elif order == "Espresso": 
    price = 6 
elif order == "Mocha": 
    price = 4.50 
elif order == "Tea": 
    price = 2 
else: 
    print ("Sorry, We don't have that here.")
    price = 0
    exit ()

# An extra if else parameter to really test our logical understanding 

if order == "Latte": 
    print ("Would you like whipped cream?") 
    answer = input ()
    if answer == "Yes":
     print (" Whipped cream costs £2 ")
else: 
    print ("Okay no whipped cream")


print ("Thanks for ordering a " + order + " " + " \nThis will be prepared for you in a few minutes. ") 

quantity = input ("How many cups of " + order + " would you like? \n ")

total = price * int(quantity)

print ("Your total is $" +  str(total)  + ". Please pay at the counter. Thank you for coming and enjoy your coffee")