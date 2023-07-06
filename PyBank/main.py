# Author: Ashley Paillet
# Project: Module 3 Challenge, PyBank
#----------------------------------------
# /Users/ashleypaillet/Desktop/git_HUB/03-python-challenge/python-challenge/PyBank
# budget_data.csv
# budget_data = '../Resources/budget_data.csv'
#
import os
import csv 
budget_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_csv, encoding='UTF-8') as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')
    budget_header = next(budget_reader)
    #
    debit_credit = 0
    months = 0
    previous_month_income = 0
    #
    net_income = 0
    #
    max_increase = 0
    max_increase_month = 0
    #
    max_decrease = 999999999999999
    max_decrease_month = 999999999999999
    #
    for row in budget_reader: 
         month_income = int(row[1])
         debit_credit = debit_credit + month_income
         months = months + 1
         #
         if months > 1:
            #
            difference = month_income - previous_month_income
            net_income = net_income + difference
            avg_diff = net_income / (months - 1)
            #
            if difference > max_increase:
                max_increase = difference
                max_increase_month = row[0]
            #    
            if difference < max_decrease:
                max_decrease = difference
                max_decrease_month = row[0]
         previous_month_income = int(row[1])
    #
    # Analysis Summary
    print('Financial Analysis')
    print('----------------------------------------')
    print(f'Total Months: {months}')
    print(f'Total: $ {debit_credit}')
    print(f'Average Change: $ {round(avg_diff, 2)}')
    print(f'Greatest Increase in Profits: {max_increase_month}: $ {max_increase}')
    print(f'Greatest Decrease in Profits: {max_decrease_month}: $ {max_decrease}')
    #
    # Export to .txt
    export_py_bank = os.path.join('analysis', 'py_bank.txt')
    with open(export_py_bank, 'w') as f:
        f.write('Author: Ashley Paillet\n')
        f.write('----------------------------------------\n')
        f.write('Financial Analysis\n')
        f.write('----------------------------------------\n')
        f.write(f'Total Months: {months}\n')
        f.write(f'Total: $ {debit_credit}\n')
        f.write(f'Average Change: $ {round(avg_diff, 2)}\n')
        f.write(f'Greatest Increase in Profits: {max_increase_month}: $ {max_increase}\n')
        f.write(f'Greatest Decrease in Profits: {max_decrease_month}: $ {max_decrease}\n')
        