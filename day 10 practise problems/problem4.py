#Problem #4
#Input is an array of strings of an arithmetic expression. Calculate the value.
#eg - input ["1", "2", "+", "5", "*"]
#output =  15
#explanation (1 + 2) * 5 = 15


#getting user input
inputString = input("Enter a postfix expression with space inbetween numbers and operators ")
expressions = inputString.split()           #making a list out of expressions
    
stack = list()                              #initializing an empty stack

operators = ["+","-","*","/","%"]           #initializing an operator list for reference

for exp in expressions :                    #initializing a for loop to calculate the solution
    
    if exp not in operators :               #pushing the operands to the stack
        stack.append(exp)

    else :                                  
        operand1 = int(stack.pop())         #poping the first operand frm stack on encountering an operator

        if not stack :                      #validating the input. Checks for empty stack.
            print("Invalid expression")
            exit(0)
        else:
                operand2 = int(stack.pop()) #poping the operansd 2 out of the stack

        #performing relevent operation as per the operator
        if exp == "+" :
            answer = operand1 + operand2
            
        elif exp == "-" :
            answer = operand1 - operand2

        elif exp == "*" :
            answer = operand1 * operand2                

        elif exp == "/" :
            if operand2 == 0 :              #validating input
                print("Invalid expression. Division operator has encountered a zero divisor")
                exit(0)

            else :
                answer = operand1 / operand2 

        elif exp == "%" :                   #validating input
            if operand2 == 0 :
                print("Invalid expression. Modulus operator has encountered a zero divisor")
                exit(0)

            else :
                answer = operand1 % operand2     


        stack.append(answer)                #pushing the answer to the stack

if len(stack) != 1 or len(stack) == 0 :     #empty stack or a stack with more than 1 element indicates invalid expression
    print("Postfix expression is invalid")

else :
    final_answer = stack.pop()
    print("Solution : " ,final_answer)       #printing final answer





# output :
# Enter a postfix expression with space inbetween numbers and operators 3 4 * 5 -
# Solution : -7


