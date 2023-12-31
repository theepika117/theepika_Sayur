# Problem #2
# Write a program that calculates the profit generated by a movie theatre for different ticket classes.

# For VIP tickets, the profit is 30% of the ticket price + Rs120 for every ticket sold.
# For General tickets, the profit is 20% of the ticket price + Rs80 for every ticket sold.
# For Matinee show tickets, the profit is a flat 15% of the ticket price.
# Input: Ticket price and number of tickets sold for each ticket class.
# Output: Calculate and print the total revenue generated by the theatre in a day.



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

# output :
# Enter the details of VIP class tickets :      
# Enter the price of a sinlge ticket : 100      
# Enter the number of tickets sold : 10
# Total profit for VIP class ticket = Rs. 1500.0

# Enter the details of General class tickets :  
# Enter the price of a sinlge ticket : 100      
# Enter the number of tickets sold : 10
# Total profit for VIP class ticket = Rs. 1000.0

# Enter the details of Matinee class tickets :  
# Enter the price of a sinlge ticket : 100      
# Enter the number of tickets sold : 10
# Total profit for VIP class ticket = Rs. 150.0 
# Total profit in a single day = Rs. 2650.0 