# print("Earned amount: \nBubblegum: $202\nToffee: $118\nIce cream: $2250\nMilk chocolate: $1680\nDoughnut: $1075\nPancake: $80\n\nIncome: $")

income = {
    "Bubblegum:": 202,
    "Toffee:": 118,
    "Ice cream:": 2250,
    "Milk chocolate:": 1680,
    "Doughnut:": 1075,
    "Pancake:": 80

}

print("Earned amount:")
for key, value in income.items():
    print(key, '$' + str(value))


sum_ = 0
for i in income.values():
    sum_ += i
    

print(f"\nIncome: ${sum_}")
staff_expenses = int(input("Staff expenses: \n"))
other_expense = int(input("Other expenses: \n"))
net_income = sum_ - (staff_expenses + other_expense)
print(f"Net income: ${net_income}")


