#! python 3

import math

#-------------------------------------------------------------------------------------
# menu for user to enter variables
#-----------------------------------------------------------------------------------

def tfmenu(controller):
    if controller == 1:
        controller = 0
        print('enter eligibility precentage as a number')
        bennies = float(int(input())) #benifits eligiblilty precentage
        print('enter total fees')
        fees = float(int(input())) #cost of all classes
        print('enter total credits')
        cred = int(input()) #total credits for the quarter
        inputcheck(bennies, fees, cred) #move to double check, use user inputs as arguments for the function
    
#----------------------------------------------------------------------------------
# annoying double check that everything has
#---------------------------------------------------------------------------------
def inputcheck(bennies, fees, cred):
    checkbens = str(bennies) #convert to string to allow for printing
    checkfees = str(fees)
    checkcred = str(cred) 
    print('you entered:')
    print('Eligibility precentage: %' + checkbens) # concantate to print variables previously converted to strings
    print('Total fees: $' + checkfees)
    print('Total credits: ' + checkcred)
    retrycheck = str(input('is this correct? \n Y/N \n'))
        
    if retrycheck == 'Y' or retrycheck == 'y':
        tfcal(bennies, fees, cred) #move to for loop

    else:
        controller = 1
        tfmenu(controller) #return to function for user to re-enter variables

#----------------------------------------------------------------------------------------
#for loop to diplay credit breakdown
#----------------------------------------------------------------------------------------
def tfcal (bennies, fees, cred):
    benniescalc = bennies / 100 #move decimal place left by 2 to setup for calculation
    feescalc = fees * benniescalc #multiply fees by eligibility precentage
    credcalc = feescalc / cred #divide fees after finding total fees multiplied by elegiliby precentage
    forcred = credcalc # creating new variable to be calculated in the for loop
    print('Total fees: $' + str(feescalc)) #concantate and convert to string for printing
    print('cost per credit: $' + str(credcalc))
    print('cost breakdown by credit:')
    for x in range(cred + 1): #loops by the number entered as total credits
        pcred = forcred * x #calculation outside the print function because print doesnt like float variables
        print(str(x) +'= $' + str(pcred)) #convert floats to strings for printing

        if x == cred:
                controller = 1
                tfmenu(controller) #end loop and return to user input


#---------------------------------------------------------------------------------
# program starts here
# --------------------------------------------------------------------------------        
if __name__ == '__main__':
    print('make a selection')
    print('1. calculate tuition and fees')
    print('2. PENUS PENUS PENUS PENUS')
    controller = int(input())
    tfmenu(controller)

#notes:
# TOTAL (resident):
# 1 - 133.09
# 2 - 246.18
# 3 - 359.27
# 4 - 472.36
# 5 - 585.45
# 6 - 698.54
# 7 - 811.63
# 8 - 924.72
# 9 - 1037.81
# 10 - 1150.90
# 11 - 1204.16
# 12 - 1257.42
# 13 - 1310.68
# 14 - 1363.94
# 15 - 1417.20
# 16 - 1470.46
# 17 - 1523.72
# 18 - 1576.98
# 19 - 1673.51
# 20 - 1770.04
# 21 - 1866.57
# 22 - 1963.10
# 23 - 2059.63
# 24 - 2156.16
# 25 - 2252.69

# - total charges, mulitply by precentage

# - total credits, divide by total
#divide by 100

# - cost per credit, multiply by credits per class

# -add class fees to specific class