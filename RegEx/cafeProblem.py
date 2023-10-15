#menu
#init store

#while loop for getting customer input
#use regex to find out what customers are asking. Get input from 10 customers
#eg - I want 3 vada and 3 coffee
#Eg give me 5 vada and 2 pepsi and 1 icecream
#check for supply each time

#end - calculate sales and profit
# Sales , profit


#importing regular expression package
import re   

#initializing menu stock and sales details lists
menu = ["vadai","tea","coffee"]         #contains menu available in the cafe
price = [10,12,15]                      #contains price of the food in the menu
stock = [50,45,40]                      #contains total number of stock available for each food for sales
sales = [0,0,0]                         #contains number of each food sold
profit = [4,5,6]                        #contains profit that we have fixed for each food items
customer_input = []                     #empty list to append customer order


#getting order from customer and checking for the availability each time and updating the sales details each time
for customers in range(10) :
    order = input("enter your order: ")                             #getting order as input
    quantity = re.findall(r'\b(\d{2}|\d+)\b' , order)               #seperating quantity of food using RegEx
    items = re.findall(r'\b(vadai|tea|coffee)\b',order.lower())     #seperating the food item ordered using RegEx
 
    #for loop to check for stock for the foods in items list 
    for index,item in enumerate(items) :
        orderedQuantity = int(quantity[index])
        x=menu.index(item)
        #child for loop to check for the availability of food ordered by the customer
        for food in menu :
            if item == food :
                x = menu.index(food)            # x stores the index of the food ordered in the menu list
                availableQuantity = int(stock[x])
                soldQuantity = sales[x]
                
                #checking for the availability of food ordered
                if orderedQuantity < availableQuantity :
                    stock[x] = availableQuantity - orderedQuantity      #updating stock list
                    sales[x] = soldQuantity + orderedQuantity           #updating sales list
                else :
                    print(f"only {stock[x]} {food} is available :" )

totalProfit = 0         #for calculating net profit

#initializing a for loop to calculate profit
for index, sale in enumerate (sales) :
    final_profit = sales [index] * profit [index]               #calculating profit for individual food item
    totalProfit += final_profit                                 #calculating net profit
    print(f"profit for {menu[index]} is {final_profit}")        #printing profit of each item

print(f"Total profit is {totalProfit}")                         #printing net profit


        
        
        
        
