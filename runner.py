from importlib.resources import path
import csv
from User import User

path = "data/costs.csv"
cat=[]
with open(path,'w') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cat.append(cat(**dict(row)))

print(cat)
