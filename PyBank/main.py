# PyBank
# /Users/ashleypaillet/Desktop/git_HUB/03-python-challenge/python-challenge/PyBank
file = '../Resources/budget_data.csv'

import os
import csv 
csvpath = os.path.join('Resources', 'budget_data.csv')

# budget_data.csv
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')
    # for row in csvreader:
    #     print(row)

print('Financial Analysis')
print('----------------------------------------')
# months = 
# print( 'Total Months: ')
# Total:
# Average Change: $
# Greatest Increase in Profits:
# Greatest Decrease in Profits
