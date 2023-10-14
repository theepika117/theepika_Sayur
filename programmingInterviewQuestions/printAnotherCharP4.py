# 



string = input("Enter a String : ")
key = int(input("Enter a key value : "))
words = string.split()                      #splitting the string into a list of individual words
newString = ''                              #initializing a new empty string


for i in range(len(words)) :                #for loop to constring new string according to the given algorithm
    temp = words[i]
    newWord = ''                            #initializing an empty string to create requred alternative word for user given word
    
    
    if (i+1)%2 != 0 :                       #checking whether the word is in odd position
        for j in range (len(temp)) :        #for loop to iterate over the particular word char by char
            char = temp[j]                  #seperating individual char
            asciiValue =  ord(char)         #determining its ASCII value
            newChr = chr(asciiValue+key)    #finding the alternative char to be printed
            newWord += newChr               #appending the char found to newWord string
    
    
    else :
        temp1 = temp[::-1]                  #generating reverse of the particular word
        for j in range (len(temp1)) :       #iterating through every chr of temp1
            char = temp1[j]                 #seperating individual char
            asciiValue =  ord(char)         #determining its ASCII value
            newChr = chr(asciiValue+key)    #finding the alternative char to be printed
            newWord += newChr               #appending the char found to newWord string
        
    
    newString = newString  + newWord + ' '  #appending newWord to newString

print(newString)



# Output :
# Enter a String : hi this is Theepika Ravikumar
# Enter a key value : 2
# jk ukjv ku cmkrggjV Tcxkmwoct