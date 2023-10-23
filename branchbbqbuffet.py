# Name: Jacob Zar
# Prog Purpose: branch bbq buffet price calc
# Price for adults: $19.95 Price for children: $11.95
# Service frr rate: 10%
# Sales Tax rate: 6.2%

import datetime

########## define global variables ###########
# define
SERVICE_RATE_FEE = .10
SALES_TAX_RATE = .062
PR_ADULT = 19.95
PR_CHILD = 11.95

# define global variables
num_adults = 0
num_children = 0
subtotal_adult = 0
subtotal_children = 0
sales_tax = 0
service_fee = 0
total = 0

########### define program functions ##############
def main():

    more_food = True

    while more_food:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order again (Y or N)?: " )
        if askAgain.upper() == "N" or askAgain == "n":
            more_food = False
            print("Thank you for your order. Enjoy your food!")

def get_user_data():
    global num_adults
    num_adults = int(input("Number of adults: "))
    global num_children
    num_children = int(input("Number of Children: "))

def perform_calculations():
    global subtotal, sales_tax, total, subtotal_adult, subtotal_children, service_fee
    subtotal_adult = num_adults * PR_ADULT
    subtotal_children = num_children * PR_CHILD
    subtotal = subtotal_adult + subtotal_children
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERVICE_RATE_FEE
    total = subtotal + sales_tax + service_fee


def display_results():
    print('----------------------')
    print('**** BRANCH BARBECUE BUFFET ****')
    print('----------------------')
    print('Adults       $ ' + format(subtotal_adult,'8,.2f'))
    print('Children     $ ' + format(subtotal_children,'8,.2f'))
    print('Subtotal     $ ' + format(subtotal,'8,.2f'))
    print('Service Fee  $ ' + format(service_fee,'8,.2f'))
    print('Sales Tax    $ ' + format(sales_tax,'8,.2f'))
    print('Total Amount $ ' + format(total,'8,.2f'))
    print('-----------------------')
    print(str(datetime.datetime.now()))

############  call on main program to execute  ############
main()


    
    
    
