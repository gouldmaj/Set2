# This code collects the data needed to calculate the total cost of a five-item sale
item1_price = float(input("Enter the price of the first item: $"))
item2_price = float(input("Enter the price of the second item: $"))
item3_price = float(input("Enter the price of the third item: $"))
item4_price = float(input("Enter the price of the fourth item: $"))
item5_price = float(input("Enter the price of the fifth item: $"))

# This code calculates the total cost of the five items with a 7% sales tax
subtotal = item1_price + item2_price + item3_price + item4_price + item5_price
sales_tax = subtotal * 0.07
total_cost = subtotal + sales_tax

# This code rounds the sales tax to two decimal places so it can be displayed as a monetary value
sales_tax = round(sales_tax, 2)
# This code rounds the subtotal to two decimal places so it can be displayed as a monetary value
subtotal = round(subtotal, 2)
# This code rounds the total cost to two decimal places so it can be displayed as a monetary value
total_cost = round(total_cost, 2)

# This code displays the subtotal to the user
print('Subtotal: $',subtotal)
# This code displays the total sales tax to the user
print('Sales tax (7%): $',sales_tax)
# This code displays the total cost to the user
print('Total: $',total_cost)