# Name: Zar & Danilo
# Prog Purpose: This program finds the cost of movie tickets
# Price for one ticket: $10.99
# Sales Tax rate: 5.5%

import datetime

########## define global variables ###########
# define
SALES_TAX_RATE = .055
PR_SMALL_PIZZA = 9.99
PR_MED_PIZZA = 12.99
PR_LARGE_PIZZA = 17.99
PR_XTRA_LARGE_PIZZA = 21.99
PR_DRINK = 3.99
PR_BREADSTX = 6.99

# define global variables
num_pizza = 0
num_drink = 0
num_breadstx = 0 
prt_pizzas = 0
prt_drinks = 0
sales_tax = 0
prt_breadstx = 0
subtotal = 0
total = 0

########### define program functions ##############
def main():

    more_pizza = True

    while more_pizza:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order more food?(Y or N)?: " )
        if askAgain.upper() == "N" or askAgain == "n":
            more_pizza = False
            print("Thank you for your order. Enjoy your food!")

def get_user_data():
    global pizza_size, num_pizza, num_drink, num_breadstx
    pizza_size = input("\nWhat size pizza would you like: Xtra-Large - 21.99(A) Large - 17.99(B) Medium - 12.99(C) Small - 9.99(D): " )
    if pizza_size.upper() == "A" or pizza_size == "a":
            pizza_size = PR_XTRA_LARGE_PIZZA
    elif pizza_size.upper() == "B" or pizza_size == "b":
        pizza_size = PR_LARGE_PIZZA
    elif pizza_size.upper() == "C" or pizza_size == "c":
        pizza_size = PR_MED_PIZZA
    elif pizza_size.upper() == "D" or pizza_size == "d":
        pizza_size = PR_SMALL_PIZZA
    else:
        print("Invalid pizza size selection. Please choose a valid option.")
        return

    num_pizza = int(input("How many pizzas of this size do you want?:"))
    num_drink = int(input("How many drinks do you want?: "))
    num_breadstx = int(input("How many orders of breadsticks do you want?: "))

def perform_calculations():
    global prt_pizzas, prt_drinks, prt_breadstx, subtotal, total, sales_tax
    prt_pizzas = pizza_size * num_pizza
    prt_drinks = num_drink * PR_DRINK
    prt_breadstx = num_breadstx * PR_BREADSTX
    subtotal = prt_pizzas + prt_drinks + prt_breadstx
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    
    


def display_results():
    print('-----------------------')
    print('**** PALERMO PIZZA ****')
    print('-----------------------')
    print('Price of Pizzas       $ ' + format(prt_pizzas,'8,.2f'))
    print('Price of Drinks       $ ' + format(prt_drinks,'8,.2f'))
    print('Price of Breadsticks  $ ' + format(prt_breadstx,'8,.2f'))
    print('Subtotal              $ ' + format(subtotal,'8,.2f'))
    print('Sales Tax             $ ' + format(sales_tax,'8,.2f'))
    print('Total Amount          $ ' + format(total,'8,.2f'))
    print('-----------------------')
    print(str(datetime.datetime.now()))

############  call on main program to execute  ############
main()
