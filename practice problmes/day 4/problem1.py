# Problem #1
# write a program that reads a passage and reverses the order of 
# letters in each word while keeping the word order intact. Use function.
# Eg- input - I am Sayur
# Output I ma ruyaS

user_input = input("Copy paste a paragraph : \n")
words = user_input.split()                              #creating a list of words
output_string = str()                                   #initialising a string to store required output
for word in words:  
    if len(word) > 1 :                                  #making sure to reverse only words with more than 1 letter
        if word[-1].isalnum() :
            temp = word[::-1]
            
        else :
            wrd = word[:-1]
            symbol = word[-1]
            temp = wrd[::-1] + symbol
        output_string = output_string + temp + " "

    else :
        output_string = output_string + word + " "

print(output_string)


# Output:
# Copy paste a paragraph :
# hi, hello how are you?
# ih, olleh woh era uoy?