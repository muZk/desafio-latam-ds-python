import sys

TAX = 0.35
price = int(sys.argv[1])
number_of_users = int(sys.argv[2])
premium_users = int(sys.argv[3])  # they pay 2x
freemium_users = int(sys.argv[4])
expenses = int(sys.argv[5])

normal_users = number_of_users - premium_users - freemium_users

income = normal_users * price + premium_users * 2 * price
revenue = income - expenses

if revenue > 0:
    revenue_after_taxes = int((1 - TAX) * revenue)
else:
    revenue_after_taxes = revenue

print(revenue_after_taxes)
