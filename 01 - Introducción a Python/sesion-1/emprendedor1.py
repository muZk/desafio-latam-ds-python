import sys

TAX = 0.35
price = int(sys.argv[1])
number_of_users = int(sys.argv[2])
expenses = int(sys.argv[3])

revenue = price * number_of_users - expenses

if revenue > 0:
    revenue_after_taxes = int((1 - TAX) * revenue)
else:
    revenue_after_taxes = revenue

print(revenue_after_taxes)
