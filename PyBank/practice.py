

# Author: Ashley Paillet
# Project: Module 3 Challenge, PyBank
# /Users/ashleypaillet/Desktop/git_HUB/03-python-challenge/python-challenge/PyBank
budget_data = '../Resources/budget_data.csv'
#
import os
import csv 
budget_csv = os.path.join('Resources', 'budget_data.csv')
#
# budget_data.csv
with open(budget_csv, encoding='UTF-8') as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')
    # print(budget_reader)
    budget_header = next(budget_reader)
    # print(f'CSV Header: {budget_header}')
    # def sum(numbers):
    def summary(budget_data):
        for row in budget_reader: 
         profit_loss_values = row[1]
        #  print(months)
        print(len(int(profit_loss_values)))
    summary(budget_data)    
    # profit_loss = []
    # profit_loss = [row for row in csvreader]
    # print(profit_loss)
    
      
    # print('Financial Analysis')
    # print('----------------------------------------')
    # #
    # print('Total Months: ')
    # print('Total: ')
    # print('Average Change: $ ')
    # print('Greatest Increase in Profits: ')
    # print('Greatest Decrease in Profits: ')
