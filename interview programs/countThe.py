#program to count the number of times the word 'the' followed by 'the' without a 'a' inbetween appears


#psuedocode
#get the passage as input from the user
#split the individual words
#iterate the entire list untill no the appears in the sliced list
#find the first occurance of 'the' , next occurance of 'the' and first occurance of 'a'
#if index of first 'a' is > second 'the' , increment the count and slice the string and continue iterating
#else slice without incrementing and continue iterating


#source code

string = input("Enter your passage / string : \n")
string = string.lower()
words = string.split()

theFound = True
count = 0

while(theFound) :
    firstTHE = words.index('the')
    if firstTHE == -1 :
        theFound = False

    else :
        findA = words.index('a')
        temp = words[firstTHE:]
        secondTHE = temp.index('the')
        if secondTHE == -1 :
            theFound = False
            break
        else :
            if findA > secondTHE :
                count += 1
                del words[:(firstTHE+1)]


print(count)

# del words[:3]
# print(words)