amounts = []
categories = []
descriptions = []
while True:
 amount = float(input("Enter amount: "))
 category = input("Enter category: ")
 description = input("Enter the description: ")
 amounts.append(amount)
 categories.append(category)
 descriptions.append(description)
 choice = input(" Do you want to add another expense? (yes/no): ")
 if choice.lower() == "no":
     break
print("\n---------All Expenses--------")
for i in range(len(amounts)):
    print(i+1 , categories[i], descriptions[i],amounts[i])
    
total = 0
for amount in amounts:
     total += amount
print("\n Total Expense :", total)

highest = amounts[0]

for amount in amounts:
    if amount > highest:
        highest = amount
print("\n Highest Expense:", highest)

lowest = amounts[0]
for amount in amounts:
    if amount < lowest:
        lowest = amount
print("\n Lowest Expense:", lowest)

average = total / len(amounts)
print("Average Expense: ", round(average,2))

