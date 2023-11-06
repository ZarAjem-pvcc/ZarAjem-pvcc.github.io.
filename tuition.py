# Name:
# Afsana Nawrozi
# Felax Barrienpos
# Zar

# prog purpose: This program computers PVCC college and fees based on number of credits
# PVCC Fee Rates are from : https://www.pvcc.edu/tuition-and-fees


import datetime
#define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 250
RATE_INSTITUITION_FEE = 1.75
RATE_ACTVITY_FEE = 2.90

#define global variables
inout = 1 # means in-state, 2 means out-of-state
num_credits = 0
scholarships = 0

tuition = 0
institiution_fee = 0
capital_fee = 0
activity_fee = 0
total= 0
balance = 0


############# define program functions ###############
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("Would you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.lower() == "n":
            more = False 
def get_user_data():
    global inout, num_credits, scholarshipamt
    inout = int(input("Enter a 1 for IN_STATE; enter a 2 for OUT_OF_STATE: "))
    num_credits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global  tuition, institiution_fee, capital_fee, activity_fee, balance, total 
    if inout== 1:
        tuition = num_credits * RATE_TUITION_IN
        capital_fee = 0
    else:
        tuition = num_credits * RATE_TUITION_OUT
        capital_fee = RATE_CAPITAL_FEE * num_credits   
        

    institiution_fee = RATE_INSTITUITION_FEE * num_credits
    activity_fee = RATE_ACTVITY_FEE * num_credits
    total = tuition + capital_fee + institiution_fee + activity_fee
    balance = total - scholarshipamt


def display_results():
    moneyformat = '8,.2f'
    line = '---------------------------------'
    print(line)
    print('**** PVCC TUITION & FEE COST****')
    print('')
    print(line)
    print('Tuition           $ ' + format(tuition, moneyformat))
    print('Capital_Fee       $ ' + format(capital_fee, moneyformat))
    print('Institiution_fee  $ ' + format(institiution_fee, moneyformat))
    print('Activity_fee      $ ' + format(activity_fee, moneyformat ))
    print('Balance           $ ' + format(balance, moneyformat))
    print('Total             $ ' + format(total, moneyformat))
    
    print(line)
    print(str(datetime.datetime.now()))
######### call on main program to execute ########
main()
    
    
    
 
  
    












    
    
    


