# program to choose between old regime and new regime of income tax calculation. 
# salaried employee can choose between these two for the given financial year. 

#getting gross salary and deductions as input

gross_salary = float(input("Enter your Gross Salary \nYour Gross salary is your salary without pf and othee deductions. \n"))

# getting the type of city as input for House Rent Allowance (hra) calculation. 
choice = input("Do you reside in Metro city (y/n) ")

#for metro city its 50% of gross salary
if choice == 'y' or choice =='Y' :
    limit = 0.50 * gross_salary
    print(limit, " is your maximum HRA limit. ", end = " ")
    hra = float(input("Enter your HRA : "))
    print(hra)
    if hra > limit :
        print("HRA cannot be greater than ", limit)
        exit(0)
    
#for non metro city its 40% of gross salary
elif choice == 'n' or choice =='N' :
    limit = 0.40 * gross_salary
    print(limit, " is your maximum HRA limit. ", end = " ")
    hra = float(input("Enter your HRA : "))
    print(hra)
    if hra > limit :
        print("HRA cannot be greater than ", limit)
        exit(0)
   
else :
    print("Not a valid entry ")
    exit(0)

#both regimes accept deductions under payment towards pension scheme for government employees. Let's get their type of employment for further calculation. 
choice = input("Are you a state government employee (y/n) : ")
if choice == 'y' or choice =='Y' :
    pension = 0.1* gross_salary

elif choice == 'n' or choice =='N' :
    choice = input("Are you a central government employee (y/n) : ")
    if choice == 'y' or choice =='Y' :
        pension = 0.14* gross_salary
      
    elif choice == 'n' or choice =='N':
        pension = 0
        
    else :
        print("Not a valid entry ")
        exit(0)

else :
    print("Not a valid entry ")
    exit(0)


'''
We have collected required inputs now let's calculate payable_tax according to old regime


According to old regime the following are the tax slabs
For first 2.5 lakhs no tax
For the range 2.5 to 5 lakh 5% tax
For the range 5 to 10 lakh 20% tax
Beyong 10 lakh 30%

Aftr this we need to calculate cess tax and add it to tax to get the payable_tax 

'''

#Old regime allows deductions under 80C, HRA and pension. 

deduction80C = 150000
deduction = hra + deduction80C + pension

# salary - deduction will give us the taxable income 
taxable_income = gross_salary - deduction 


# determining tax slab on the basis of taxable income

if taxable_income <= 250000 :
    tax = 0
    
elif taxable_income > 250000 and taxable_income <= 500000 :
    amount = taxable_income - 250000
    tax = amount * 0.05
    
elif taxable_income > 500000 and taxable_income <= 1000000 :
    amount = taxable_income - 500000
    tax1 = amount * 0.20
    tax2 = 250000 * 0.05
    tax = tax1 + tax2
    
else :
    amount = taxable_income - 1000000
    tax1 = amount * 0.30
    tax2 = 250000 * 0.05
    tax3 = 500000 * 0.20
    tax = tax1 + tax2 + tax3
    
    
#calculating medical and education cess
cess_tax = tax * 0.04

# calculating net payable tax
payable_tax_oldRegime = tax + cess_tax


'''
now let's calculate payable_tax according to new regime


According to new regime the following are the tax slabs
For first 3 lakhs no tax
For the range 3 to 6 lakh 5% tax
For the range 6 to 9 lakh 10% tax
For the range 9 to 12 lakh 15% tax
For the range 12 to 15 lakh 20% tax
Beyond 15 lakh 30%

Aftr this we need to calculate cess tax and add it to tax to get the payable_tax 

'''

#new regime allows only deduction under payment towards pension
deduction = pension

# salary - deduction will give us the taxable income 
taxable_income2 = gross_salary - deduction 


# determining tax slab on the basis of taxable income

if taxable_income2 <= 300000 :
    tax = 0
    
elif taxable_income2 > 300000 and taxable_income2 <= 600000 :
    amount = taxable_income2 - 300000
    tax = amount * 0.05
    print(tax)

elif taxable_income2 > 600000 and taxable_income2 <= 900000 :
    amount = taxable_income2 - 600000
    tax1 = amount * 0.10
    tax2 = 300000 * 0.05
    tax = tax1 + tax2 
    
elif taxable_income2 > 900000 and taxable_income2 <= 120000 :
    amount = taxable_income2 - 900000
    tax1 = amount * 0.15
    tax2 = 300000 * 0.05
    tax3 = 300000 * 0.10
    tax = tax1 + tax2 +tax3 
    
elif taxable_income2 > 120000 and taxable_income2 <= 150000 :
    amount = taxable_income2 - 120000
    tax1 = amount * 0.20
    tax2 = 300000 * 0.05
    tax3 = 300000 * 0.10
    tax4 = 300000 * 0.15
    tax = tax1 + tax2 + tax3 + tax4
    
else :
    amount = taxable_income2 - 150000
    tax1 = amount * 0.30
    tax2 = 300000 * 0.05
    tax3 = 300000 * 0.10
    tax4 = 300000 * 0.15
    tax5 = 300000 * 0.20
    tax = tax1 + tax2 + tax3 + tax4 + tax5

#calculating medical and education cess
cess_tax2 = tax * 0.04

# calculating net payable tax
payable_tax_newRegime = tax + cess_tax2
  
  
# printing both results
print("Your calculated Tax according to old regime is ₹",payable_tax_oldRegime)
print("Your calculated Tax according to old regime is ₹",payable_tax_newRegime)

#suggesting them the better choice 
if payable_tax_oldRegime >  payable_tax_newRegime :
    print("You can choose new regime for this financial year as it reduces your income tax than the old regime. ")
    
elif payable_tax_oldRegime < payable_tax_newRegime :
    print("You can choose old regime for this financial year as it reduces your income tax than the new regime. ")
    
else :
    print("You can choose any one as both yields same amount of income tax to be paid")
    
    
    



# Output:

# Enter your Gross Salary 
# Your Gross salary is your salary without pf and othee deductions. 
# 700000
# Do you reside in Metro city (y/n) y
# 350000.0  is your maximum HRA limit.  Enter your HRA : 50000
# 50000.0
# Are you a state government employee (y/n) : y
# Your calculated Tax according to old regime is ₹ 9360.0
# Your calculated Tax according to old regime is ₹ 18720.0
# You can choose old regime for this financial year as it reduces your income tax than the new regime. 
# >
