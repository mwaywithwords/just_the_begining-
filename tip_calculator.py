'''
my tip calculator will ask the patrons to enter the cost of their meal, the number of people splitting the bill, and how much they are willing or able to tip percentage wise. the calculator will then give the user the total of the bill (tip included) and the sum each person is required to pay.
'''
'''veriables that must be created 
"the amount of the bill(user imputted)\n
the amount of tax included(fixed percantage)\n
the amount of people splitting the bill.\n
the amount of taxes combined coming from the total bill\n
the tip precentage that the petron would like to tip\n 
the number of people that will be splitting said bill, the total of the food cost + tax and tip, devided by the number of people splitting the bill'''"

'''decleared veriables'''
# i used a float because i figured most bills will come up as a float instead of an int . 
food_cost = float(input("please enter the cost of your meal"))
#i will also use a float here in my tip percentage because of simular reasoning as the my food cost as my food_cost veriable.
tip_prcentage = float(input("how much in percentage will you be tipping?"))
# to ensure that the logic behind my choice of floats over int is applied, i will insert a while loop to produce and error message when anything that is not a float is used.
while tip_prcentage >1:
    print("error! please enter decimal to reflect desired tip amount.")
    tip_prcentage = float(input('how much would you be tipping?'))

number_of_petrons = int(input('how many will you be splitting the tab?'))
tax = .10

# calculation of the tip amount
'''here we creat formulas to calculate the tip amount of the bill once split'''

# tip amount is the food cost * tip percentage
tip_amount = food_cost * tip_prcentage
# total taxed amount is the food cost * tax 
total_taxed_amount = food_cost * tax
# total would be adding tax + food cost + tip amount to come up with the total bill cost.
total_bill = total_taxed_amount + food_cost + tip_amount
# to produce the individual total we / the total bill and the number of patrons. 
individual_total = total_bill / number_of_petrons

# the results
print(f' your total with tax and your genorous tip included comes up to $ {total_bill}')

print(f'the total amount each petron should pay is $ {individual_total}')




