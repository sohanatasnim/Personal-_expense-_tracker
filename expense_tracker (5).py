# expense_tracker.py
import csv

def add_expense(date, category, amount):
    with open('expenses.csv', 'a', newline='') as f:
        w = csv.writer(f)
        w.writerow([date, category, amount])
