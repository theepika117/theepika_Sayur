#Add two number represented in a list. print the sum also as a list in reverse order


#getting user input and converting it into a list
numbers = input("Enter numbers of list 1 in ascending order with space between every number : ")
list1 = numbers.split()

numbers = input("Enter numbers of list 1 in ascending order with space between every number : ")
list2 = numbers.split()

len1,len2 = len(list1),len(list2)

number1,number2 = 0,0

finalList = list()

for number in list1:
    number1 = (number1*10) + int(number)

for number in list2:
    number2 = (number2*10) + int(number)

sumOfList = number1 + number2

sumOfList = str(sumOfList)

limit = len(sumOfList)

for i in range(limit-1,-1,-1) :
    finalList.append(sumOfList[i])

print(finalList)


# output :
# Enter numbers of list 1 in ascending order with space between every number : 1 2 3
# Enter numbers of list 1 in ascending order with space between every number : 4 5 6
# ['9', '7', '5']

