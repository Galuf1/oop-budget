import csv
from tempfile import gettempprefix
from unicodedata import category

class User:
    def __init__(self, name):
        self.name = name
        self._income = 0
        self._categories = {}


    def __str__(self):

        return f"Your monthly budget is {self.budget}"

    @property
    def income(self):
        return self._income

    # @income.setter
    def new_income(self, new_income):
        if new_income > self.monthly_costs():
            self._income = new_income
        else: 
            print("can't do")

    @property
    def categories(self):
        return self._categories

    # @categories.setter
    def new_categorie(self, cat, amount):
        self.categories[cat] = int(amount)
        self._income -= int(amount)
    
    def expense(self,cat, expense):
        if self.categories[cat] > int(expense):
            self.categories[cat] -= int(expense)
        else:
            print("not enough budget in that category")

    def monthly_costs(self):
        sum = 0
        for i in self.categories:
            sum += self.categories.get(i,0)
        return sum
    
    def add_category(self, new_cat):
        self._categories[new_cat] = 0
    
    def get_all_percentages(self):
        for i,j in self._categories.items():
            percent = str(round((j/self._income),2))
            print(f"{i} {percent}%")


    