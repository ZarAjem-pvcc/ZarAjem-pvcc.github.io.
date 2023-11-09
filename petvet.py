# Name: Balthazar Ajemian
# Prog Purpose: This Program finds the cost of pet vaccines & medications for dogs and cats
#

import datetime

############## define global variables ##############
# define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48
PR_LEPTO = 21
PR_LYME = 41


PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

#define cat variables
PR_LEUK = 35
PR_RHINO = 30
PR_RABIES = 25
PR_FULL_VAX = 0

PR_CHEWS = 8

#define global variables

vax_cost = 0
pet_vax_type = 0
chews_cost = 0
num_chews = 0
pet_weight = 0




############## define program functions ##############
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()

        askAgain = input("\nWould you like to process another pet (Y/N)?: ")
        if askAgain.upper() == "N" :
                more = False
                print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications. ')

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet name: ")
    pet_type = input("is this pet a dog (D) or cat (C)? ")
    pet_weight = input("weight of your pet (in pounds): ")

############## DOG functions ##############

def get_dog_data():
    global pet_vax_type, num_chews
    dog1 = "n** Dog Vaccines: \n\t1.Bordatella \n\t2.DAPP \n\t3.Influenza \n\t4.Leptospirosis"
    dog2 = "nt5.Lyme Disease \n\t6.Rabies \n\t7.Full Vaccine Package \n\t8.None"
    dogmenu = dog1 + dog2
    pet_vax_type = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all dogs.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heartworm chews would you like to order? "))

def perform_dog_calculations():
    print("DOG CALCS")
    global vax_cost, chews_cost, total

    ##### vaccines

    if pet_vax_type == 1 :
        vax_cost = PR_BORD

    elif pet_vax_type == 2  :
        vax_cost = PR_DAPP

    elif pet_vax_type == 3 :
        vax_cost = PR_FLU

    elif pet_vax_type == 4 :
        vax_cost = PR_LEPTO

    elif pet_vax_type == 5 :
        vax_cost = PR_LYME

    elif pet_vax_type == 6 :
        vax_cost = PR_RABIES

    elif pet_vax_type == 8 :
        vax_cost = 0

    else:
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU + PR_LEPTO + PR_LYME + PR_RABIES
        vax_cost = .85 * PR_ALL

    ##### heart worm chews
    if num_chews != 0 :
        if int(pet_weight) < 25:
            chews_cost = num_chews * PR_CHEWS_SMALL

        elif pet_weight >= 26 and pet_weight < 50 :
            chews_cost = num_chews * PR_CHEWS_MED

        else:
            chews_cost = num_chews * PR_CHEWS_LARGE

    #####find total
        total = vax_cost + chews_cost
    
    

def display_dog_results():
    
    print('-----------------------')
    print('**** PET CARE MEDS ****')
    print('-----------------------')
    print('Chews                 $ ' + format(chews_cost,'8,.2f'))
    print('Vaccines              $ ' + format(vax_cost,'8,.2f'))
    print('Total Amount          $ ' + format(total,'8,.2f'))
    print('-----------------------')
    print(str(datetime.datetime.now()))

############## CAT functions ##############

def get_cat_data():
    print("CAT DATA")
    global pet_vax_type, num_chews
    cat1 = "n** Cat Vaccines: \n\t1.Leukemia \n\t2.Viral Rhinotracheitis \n\t3.Rabies \n\t4. Full Vaccine Package \n\t5.None"
    catmenu = cat1
    pet_vax_type = int(input(catmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all cats.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heartworm chews would you like to order? "))
    
    
    
def perform_cat_calculations():
    global vax_cost, chews_cost, total

    ##### vaccines

    if pet_vax_type == 1 :
        vax_cost = PR_LEUK

    elif pet_vax_type == 2  :
        vax_cost = PR_RHINO

    elif pet_vax_type == 3 :
        vax_cost = PR_RABIES

    elif pet_vax_type == 5 :
        vax_cost = 0

    else:
        PR_FULL_VAX = PR_LEUK + PR_RHINO + PR_RABIES
        vax_cost = .90 * PR_FULL_VAX

    ##### heart worm chews
    chews_cost = PR_CHEWS * num_chews

    #####find total
    total = vax_cost + chews_cost
    

def display_cat_results():
    print('-----------------------')
    print('**** PET CARE MEDS ****')
    print('-----------------------')
    print('Chews                 $ ' + format(chews_cost,'8,.2f'))
    print('Vaccines              $ ' + format(vax_cost,'8,.2f'))
    print('Total Amount          $ ' + format(total,'8,.2f'))
    print('-----------------------')
    print(str(datetime.datetime.now()))

main()





    
