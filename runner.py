from cmath import exp
from importlib.resources import path
import csv
from User import User

# path = "data/costs.csv"
# cat=[]
# with open(path,'w') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         cat.append(cat(**dict(row)))

# print(cat)


def main():
    Jon = User("Jon")
    
    prompt = True
    while(prompt):
        choice = input(f"Welcome Jon, your current balance is {Jon.income}\n1.- Set your income\n2.- Add category\n3.- Set budget for category\n4.- Add expense\n5.- Monthly expenses total\n6.- Monthly expenses detailed\n7.- Quit\n")

        if choice == '7':
            prompt = False
        elif choice == '1':
            amount = int(input("What's your new income\n"))
            Jon.new_income(amount)
        elif choice == '2':
            name = input("What's the name of the category\n")
            Jon.add_category(name)
        elif choice == '3':
            set_amount = input("Name the category and the amount\n").split(" ")
            Jon.new_categorie(set_amount[0],set_amount[1])
            
        elif choice == '4':
            expense = input("Add category and amount").split(" ")
            Jon.expense(expense[0],expense[1])
        elif choice == '5':
            Jon.monthly_costs()
        elif choice == '6':
            Jon.get_all_percentages()
        
main()