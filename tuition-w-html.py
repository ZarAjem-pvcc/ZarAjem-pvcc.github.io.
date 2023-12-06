# Name:
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

outfile = 'tuition-webpage.html'

############# define program functions ###############
def main():
    open_outfile()
    more = True
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()
        
        yesno = input("Would you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.lower() == "n":
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Tuition Cost Calc </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #455f98; background-image: url(wp-tuition.jpg); color: #000000;">\n')
    
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


def create_output_file():
    moneyformat = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

#   html data
    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "



    f.write('\n<table border="3"   style ="background-color: #fc6d6d;  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2> OZZY OZ TUITION CALC   </h2></td></tr>')
    f.write(colsp + '\n')

    
    f.write('**** PVCC TUITION & FEE COST****')

    f.write(tr + 'Tuition' + endtd + format(tuition, moneyformat) + endtr)
    f.write(tr + 'Capital_Fee' + endtd + format(capital_fee, moneyformat) + endtr)
    f.write(tr + 'Institiution_fee' + endtd + format(institiution_fee, moneyformat) + endtr)
    f.write(tr + 'Activity_fee' + endtd +  format(activity_fee, moneyformat )+ endtr)
    f.write(tr + 'Balance' + endtd + format(balance, moneyformat) + endtr)
    f.write(tr + 'Total' + endtd + format(total, moneyformat) + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')

main()
    
    
    
 
  
    












    
    
    


