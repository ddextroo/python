# Create a C program that will require the user
# to input Product number, Description, Quantity and Unit Price
# and would compute the discount amount of the product based on the
# following rate table:
# Quantity Rate
# Less than or equal 5 but not zero 3%
# over 5 but not over 10 5%
# over 10 but not over 15 7%
# over 15 10%
# Compute the Total amount, Discount Amount, Net Payable, and
# display. Use NESTED IF

product_no = input("Enter product number\n")
product_description = input("Enter description\n")
product_quantity = int(input("Enter quantity\n"))
unit_price = float(input("Enter unit price\n"))

if product_quantity <= 5 and product_quantity != 0:
    rate = 3/100
elif product_quantity > 5 and product_quantity <= 10:
    rate = 5/100
elif product_quantity > 10 and product_quantity <= 15:
    rate = 7/100
elif product_quantity > 15:
    rate = 10/100
else:
    print("Invalid")
    
total = float(product_quantity * unit_price)
discount = float(round(total * rate, 2))
net_payable = total - discount

print("Total: " + str(total) + "\nDiscount: " + str(discount) + "\nNet Payable: " + str(net_payable))