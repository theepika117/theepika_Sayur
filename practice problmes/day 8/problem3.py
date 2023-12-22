# Problem #3

# Same as above. But, from profit, entertainmant tax need to be subtracted. 
# Tax is 5% of the cost of the ticket.

#seperate function to calculate profit

def profitCalculator (clas,price,no) :

    #using match to calculate profit according to the ticket class
    match clas :
        case 'VIP' :
            profitPerTicket = 0.30 * price
            additionalProfit = no * 120
            totalProfit = (profitPerTicket*no) + additionalProfit

        case 'general':
            profitPerTicket = 0.20 * price
            additionalProfit = no * 80
            totalProfit = (profitPerTicket*no) + additionalProfit           

        case 'Matinee':
            profitPerTicket = 0.15 * price
            totalProfit = profitPerTicket*no
    
    tax = 0.05 * totalProfit
    totalProfit -= tax
    
    return totalProfit

#seperate function to get user input

def userInput() :
    
    price = int(input("Enter the price of a sinlge ticket : "))
    num = int(input("Enter the number of tickets sold : "))
    return price,num


#main code

totalProfit = 0
print("Enter the details of VIP class tickets : ")
price,num = userInput()
profit = profitCalculator('VIP',price,num)
print("Total profit for VIP class ticket = Rs.",profit)
totalProfit += profit

print("Enter the details of General class tickets : ")
price,num = userInput()
profit = profitCalculator('general',price,num)
print("Total profit for VIP class ticket = Rs.",profit)
totalProfit += profit

print("Enter the details of Matinee class tickets : ")
price,num = userInput()
profit = profitCalculator('Matinee',price,num)
print("Total profit for VIP class ticket = Rs.",profit)
totalProfit += profit

print("Total profit in a single day = Rs.",totalProfit)


# Output :
# Enter the details of VIP class tickets :    
# Enter the price of a sinlge ticket : 100    
# Enter the number of tickets sold : 10
# Total profit for VIP class ticket = Rs. 1425.0
# Enter the details of General class tickets :

# Enter the price of a sinlge ticket : 100    
# Enter the number of tickets sold : 10
# Total profit for VIP class ticket = Rs. 950.0
# Enter the details of Matinee class tickets :
# Enter the price of a sinlge ticket : 100    
# Enter the number of tickets sold : 10
# Total profit for VIP class ticket = Rs. 142.5
# Total profit in a single day = Rs. 2517.5 