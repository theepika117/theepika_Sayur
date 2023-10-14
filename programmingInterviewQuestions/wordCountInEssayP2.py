#2. You are writing an essay. You don't want the any word to appear very frequently. Write a program that will take your essay as input (maybe from a file) and 
#print the number of times each unique word appears in your essay.


from collections import Counter                                                 #


essay = input("Copy paste your essay here \n")

essay = essay.lower()                                                              #to avoid case sensitive confuison

words = essay.split()                                                              #creating a list of individual words from given essay

word_count = Counter(words)                                                        #creating a dictionary with words as key and their count as value

print("Following is the number of times each word appears in the essay :")

for word in word_count :

    print(word," : ",word_count[word])                                             #prints words and their count


# Output
# Copy paste your essay here
# hi this is Theepika Ravikumar. this is my test case 1.
# Following is the number of times each word appears in the essay :
# hi  :  1
# this  :  2
# is  :  2
# theepika  :  1
# ravikumar.  :  1
# my  :  1
# test  :  1
# case  :  1
# 1.  :  1