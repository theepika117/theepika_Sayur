# Problem #1.
# Write a program for calculating the profit for railways.
# For first class tickets, the profit is 25% of the price + Rs100 for every ticket sold.
# For Second class tickets, the profit is 15% of the price + Rs70 for every ticket sold.
# For Third class tickets (i don't know if there is a third class), the profit is 5% of the price.

# Get the price and no of tickets sold for each class and calculate the total profit. 
# Identity what calculation in the above problem can be written as a function 
# and what the input and output should be.


#seperate function to calculate profit

def profitCalculator (clas,price,no) :

    #using match to calculate profit according to the ticket class
    match clas :
        case 1 :
            profitPerTicket = 0.25 * price
            additionalProfit = no * 100
            totalProfit = (profitPerTicket*no) + additionalProfit

        case 2 :
            profitPerTicket = 0.15 * price
            additionalProfit = no * 70
            totalProfit = (profitPerTicket*no) + additionalProfit           

        case 3 :
            profitPerTicket = 0.05 * price
            totalProfit = profitPerTicket*no
    
    return totalProfit


#seperate function to get user input

def userInput() :
    clas = int(input("Enter class (1/2/3) : "))
    price = int(input("Enter the price of a sinlge ticket : "))
    num = int(input("Enter the number of tickets sold : "))
    return clas,price,num


#main code 

while(True):
    a,b,c = userInput()
    print("Profit = Rs.",profitCalculator(a,b,c))
    choice = input("Do you want to add more (y/n) : ")
    choice.lower()
    if choice != 'y' :
        break

    
# output :
# Enter class (1/2/3) : 1
# Enter the price of a sinlge ticket : 100
# Enter the number of tickets sold : 10
# Profit = Rs. 1250.0
# Do you want to add more (y/n) : y
# Enter class (1/2/3) : 2
# Enter the price of a sinlge ticket : 100
# Enter the number of tickets sold : 10
# Profit = Rs. 850.0
# Do you want to add more (y/n) : y
# Enter class (1/2/3) : 3
# Enter the price of a sinlge ticket : 100
# Enter the number of tickets sold : 10
# Profit = Rs. 50.0
# Do you want to add more (y/n) : n

