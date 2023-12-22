# Problem #3 
# Add two number represented in a list as reversed. print the sum also as a list in reverse order
# eg input list1 = [1,2,3] list2 = [5,6,7]
# answer= [6,8,0,1]
#  explanation (321 + 765 = 1086)

#getting user input and converting it into a list
numbers = input("Enter numbers of list 1 in ascending order with space between every number : ")
list1 = numbers.split()
list1.reverse()

numbers = input("Enter numbers of list 1 in ascending order with space between every number : ")
list2 = numbers.split()
list2.reverse()

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


# Output:
# Enter numbers of list 1 in ascending order with space between every number : 1 2 3
# Enter numbers of list 1 in ascending order with space between every number : 4 5 6
# ['5', '7', '9']

# if add_list>=10:
#             remainder = add_list % 10
#             carry = add_list // 10
#             add.append(remainder)
#             add.append(carry)