expenses = {}

while True:
    expense_name = input('Enter the name of the expense: ')
    if expense_name == 'done':
        break
    expense_amount = float(input('Enter the amount of the expense: '))
    
    expenses[expense_name] = expense_amount

total_expenses = sum(expenses.values())
print(f'Total expenses: ${total_expenses:.2f}')