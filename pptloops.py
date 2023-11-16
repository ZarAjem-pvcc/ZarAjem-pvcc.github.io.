# Name: Balthazar Ajemian
# Program Purpose: This program uses lists to find the personal property tax for vehicles in Charlottesville
#   and produces a report which displays all data and total tax due
#
# Personal property tax in Charlottesville
#       --$4.20 per $100 of vehicle value (4.20% per year
#       --Paid every six months
# Perosnal Property Tax Relief (PPTR):
#       --Eligibility: Owned or leased vehicles which are predominately used for non-business purposes & have passenger license plates
#       --Tax Relief for qualified vehicles is 33%

import datetime

################# define tax rates ##################
PPT_RATE = .042
RELIEF_RATE = .33

assessdval = 0
annual_tax_amt = 0
biannual_tax_amt = 0
relief = 0
total = 0
eligible = 0



################## define program functions #############

def main():
        more_vehicles = True

        while more_vehicles:
            get_user_data()
            perform_calculations()
            display_results()

            askAgain = input("\nWould you like to process another vehicle?(Y or N)?: " )
            if askAgain.upper() == "N" or askAgain == "n":
                more_vehicles = False
                print("Thank you for ,your time. Have a nice day")

def get_user_data():
    global assessdval, eligible, relief
    assessdval = int(input("\nWhat is the assessed value of your vehicle?:"))
    eligible = input("\nAre you eligible for tax relief (Y or N)?")
    

def perform_calculations():
    global annual_tax_amt, biannual_tax_amt, total, relief
    annual_tax_amt = assessdval * PPT_RATE
    biannual_tax_amt = annual_tax_amt / 2
    if eligible == "Y" or eligible == "y":
        relief = biannual_tax_amt * RELIEF_RATE
    else:
        relief = 0

    total = biannual_tax_amt - relief
    

def display_results():
    print('--------------------------------------')
    print('**** PERSONAL PROPERTY TAX REPORT ****')
    print('--------------------------------------')
    print('ASSESSED VALUE                      $ ' + format(assessdval,'8,.2f'))
    print('FULL ANNUAL AMOUNT                  $ ' + format(annual_tax_amt,'8,.2f'))
    print('--------------------------------------')
    print('BI-ANNUAL AMOUNT                    $ ' + format(biannual_tax_amt,'8,.2f'))
    print('RELIEF AMOUNT                       $ ' + format(relief,'8,.2f'))
    print('TOTAL AMOUNT                        $ ' + format(total,'8,.2f'))
    print('--------------------------------------')
    print(str(datetime.datetime.now()))





    
main()











    
