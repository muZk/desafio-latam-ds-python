import sys

TAX = 0.35
price = int(sys.argv[1])
number_of_users = int(sys.argv[2])
expenses = int(sys.argv[3])

if len(sys.argv) > 4:
    last_year_revenue = int(sys.argv[4])
else:
    last_year_revenue = 1000

income = price * number_of_users
revenue = income - expenses

if revenue > 0:
    revenue_after_taxes = int((1 - TAX) * revenue)
else:
    revenue_after_taxes = revenue

print(revenue_after_taxes + last_year_revenue)
