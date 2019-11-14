#determines the taxable income and income tax for an employee
#set the varibles as global by not placing them within any function
gross = float(input('Enter the gross income: '))
depen = float (input('Enter the number of dependents: '))
name = input('Enter your name: ')

def determineTaxable(gross, depen):#takes two paramters so will perform fuction on your gross as well as your depen
    taxable = gross-10000-(depen*2000)
    return taxable #gotta return it otherwise the function will not deliver the results
#taxableIncome
taxable = determineTaxable(gross, depen)# function saved within the variable
#incomeTax
incomeTax = taxable*.20 #

print(name, "your taxable income is", "$", str(format(taxable,',.2f')))
print('And your income tax is', "$", str(format(incomeTax,',.2f')))
