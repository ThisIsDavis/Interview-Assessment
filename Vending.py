# author: Davis Hwa Ye Xuan

import math
# import random

    # List of available drinks
    # drinks = [
    #     "Coca cola", "Sprite", "Mountain Dew", 
    #     "Vida Orange", "Vida Lemon", "Vida Grape", 
    #     "7UP", "Tropicana Twister", "A&W"
    # ]

    #randomly allocate prices for each drink, will save final price later. 
    # drink_prices = {drink: random.randint(1, 5) for drink in drinks}

def vendingMachine():
    # drink and respective price are stored in a dictionary
    drinkPriceDict = {'Coca cola': 2, 'Sprite': 1, 'Mountain Dew': 4, 'Vida Orange': 3, 'Vida Lemon': 5, 'Vida Grape': 1, '7UP': 5, 'Tropicana Twister': 5, 'A&W': 1}
    flag= True
    #to loop the machine program until user says "N"
    while flag:
        flag = True
        print("Available drinks and prices:")
        for drink, price in drinkPriceDict.items():
            print(f"{drink}: RM{price}")

        drinkSelectInput = input("Please select your drink: ")

        if drinkSelectInput in drinkPriceDict:
            selectedPrice = drinkPriceDict[drinkSelectInput]
            # cash input from the user
            cashInput = int(input("Please insert cash (Rm 1, 5, 10, 20, 50, 100): "))
            if cashInput >= selectedPrice:
                # Calculate change
                change = cashInput - selectedPrice
                print(cashChange(change))
            else:
                print("Insufficient funds. Please insert more cash.")
        else:
            print("Invalid drink selected, please select again.")
        toContinue = input("Would you like to purchase another drink?(Y/N): ")
        if toContinue == "Y":
            continue
        elif toContinue =="N":
            flag = False
        else:
            print("Invalid choice.")
            break

            


#####Helper Function#######
#Most efficient and accurate.
#bottom up solution
def cashChange(amount:int):
    #save a copy of inserted cash int for cash note used list print out
    savedAmountValue = amount
    myrNotes= [1,5,10,20,50,100]
    #define list with size amount+1
    dp = [math.inf] * (amount + 1)    # assuming amount=10 [10],... * number of amount+1    #base solution
    dp[0] = 0
    #min value is dp[1] = 1
    #a list of cash to return
    allCashUsed = [-1] * (amount+1)

    for a in range(1, amount+1):
        for myr in myrNotes:
            if a - myr >= 0: #not negative, continue searching
                dp[a] = min(dp[a], 1 + dp[a-myr]) #assume a=8, myr=5:  dp[8] = min(dp[8], 1 (1 myr5 note)+ dp[3])
                allCashUsed[a] = myr #save the cash note used at each solution
    #for case where no combination is found
    if dp[amount] == math.inf:
        return -1
    else:
        change =[]
        #to add used cash notes into a list to print out with back tracking
        while savedAmountValue>0:
            cash = allCashUsed[savedAmountValue]
            change.append(cash)
            savedAmountValue -= cash
                
    return "Your change is: " + str(change) + ", Number of notes returned: " +str(dp[amount]) 
    # return dp[amount]



vendingMachine()

