#menu
#init store

#use dictionary
#use regex to find out what customers are asking. Get input from 10 customers
#eg - I want 3 vada and 3 coffee
#Eg give me 5 vada and 2 pepsi and 1 icecream
#check for supply each time

#end - calculate sales and profit
# Sales , profit


#importing regular expression package
import re   


#initializing menu stock and sales details dictionary. contains menu available in the cafe
menu = {      
    "vadai" : {"price" : "10", "Stock" : "50","Sales" : "0","Profit": "4"},
    "tea" : {"price" : "12", "Stock" : "50","Sales" : "0","Profit": "5"},
    "coffee" : {"price" : "15", "Stock" : "50","Sales" : "0","Profit": "6"}
}
customer_input = []                                                 #empty list to append customer order


#getting order from customer and checking for the availability each time and updating the sales details each time
for customers in range(10) :
    order = input("enter your order: ")                             #getting order as input
    quantity = re.findall(r'\b(\d{2}|\d+)\b' , order)               #seperating quantity of food using RegEx
    items = re.findall(r'\b(vadai|tea|coffee)\b',order.lower())     #seperating the food item ordered using RegEx

    #for loop to check for stock for the foods in items list 
    for index,item in enumerate(items) :
        orderedQuantity = int(quantity[index])                      #Quantity ordered by customer. Seperate variable has been created to overcome type conversion error at runtime.
        availableQuantity = int(menu[item]['Stock'])                #quantity available in stock. Seperate variable has been created to overcome type conversion error at runtime.
        soldQuantity = int(menu[item]['Sales'])                     #quantity so far sold. Seperate variable has been created to overcome type conversion error at runtime.
        
        if orderedQuantity <= availableQuantity :                   #checking stock availability
            availableQuantity -= orderedQuantity                    
            soldQuantity += orderedQuantity
            menu[item]['Stock'] = availableQuantity                 #updating stock availability in the dictionary
            menu[item]['Sales'] = soldQuantity                      #updating sales in the dictionary

        else :
            print(f"only {availableQuantity} {item} is available :" ) 
        
totalProfit = 0
totalSales = 0                                                      #initializing variables to calculated total profit and total money made

for key in menu :                                                   #for loop has been initialized to calculate profit

    profit = int(menu[key]["Profit"]) * int(menu[key]["Sales"])     #calculating individual profit
    moneyEarned = int(menu[key]["Sales"]) *int(menu[key]["price"])  #calculating individual sales amount
    print(f"Total sales for {key} is {moneyEarned}")
    print(f"Total profit for {key} is {profit}")                    #printing both the calculated amount
    totalProfit += profit                                           #updating total profit
    totalSales += moneyEarned                                       #updating total sales

print(f"Total Sales  = {totalSales}")
print(f"Total profit = {totalProfit}")


#Output:
# enter your order: 2 coffee
# enter your order: 2 vadai
# Total sales for vadai is 20
# Total profit for vadai is 8
# Total sales for tea is 0
# Total profit for tea is 0
# Total sales for coffee is 30
# Total profit for coffee is 12
# Total Sales  = 50
# Total profit = 20


# menu = ["vadai","tea","coffee"]         #contains menu available in the cafe
# vadai = {"price" : "10", "Stock" : "50","Sales" : "0","profit": "4"}
# tea = {"price" : "12", "Stock" : "50","Sales" : "0","profit": "5"}
# coffee = {"price" : "15", "Stock" : "50","Sales" : "0","profit": "6"}
# customer_input = []         