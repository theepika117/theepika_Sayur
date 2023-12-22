# Program 2
# Given a collection of two numbers that specify an interval, merge all overlapping intervals. 
# For example, 
# Input [[1,3],[2,6],[8,10],[15,20],[16,25] ]
# Output [[1,6],[8,10],[15,25]].


nestedList = list()                     #initializing a list to store user input
mergedList = list()                     #initializing a list to store answers


#getting user input
while(True):
    num  = input("Enter an interval with black space between two numbers : ")
    interval = num.split()
    nestedList.append(interval)
    choice = input("Do u wnat to add another interval (y/n) : ")
    choice.lower()
    
#validating input
    if choice == 'n' :
        break
    elif choice != 'y' :
        print("Invalid entry ")
        break


mergedList.append(nestedList[0])                        #1st interval is considered as it has not overlapped with the next interval and it is added to the merged list

for i in range (1,len(nestedList)) :                    #initializing a for loop to run from second interval till the end
    
    if mergedList[-1][1] >= nestedList[i][0] :          #checking for overlapping interval 
        mergedList[-1][1] = nestedList[i][1]            #updating the merged list

    else :                                              #else appending the interval as such
        mergedList.append(nestedList[i])    



print(mergedList)




# output:
# Enter an interval with black space between two numbers : 1 3
# Do u wnat to add another interval (y/n) : y
# Enter an interval with black space between two numbers : 2 6
# Do u wnat to add another interval (y/n) : y
# Enter an interval with black space between two numbers : 8 10
# Do u wnat to add another interval (y/n) : y
# Enter an interval with black space between two numbers : 15 20
# Do u wnat to add another interval (y/n) : y
# Enter an interval with black space between two numbers : 16 25
# Do u wnat to add another interval (y/n) : n 
# [['1', '6'], ['8', '10'], ['15', '25']]



