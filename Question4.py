# This code collects the data needed to calculate the total cost of a five-item sale
item1_price = float(input("Enter the price of the first item: $"))
item2_price = float(input("Enter the price of the second item: $"))
item3_price = float(input("Enter the price of the third item: $"))
item4_price = float(input("Enter the price of the fourth item: $"))
item5_price = float(input("Enter the price of the fifth item: $"))

# This code calculates the total cost of the five items with a 7% sales tax
total_cost = (item1_price + item2_price + item3_price + item4_price + item5_price) * 1.07

# This code rounds the total cost to two decimal places so it can be displayed as a monetary value
total_cost = round(total_cost, 2)

# This code displays the total cost to the user
print('The total cost of your purchase is $',total_cost,)