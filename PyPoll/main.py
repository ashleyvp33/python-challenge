# Ashley Paillet
# PyPoll
# /Users/ashleypaillet/Desktop/git_HUB/03-python-challenge/python-challenge/PyPoll
file = '../Resources/election_data.csv'

import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')
    # for row in csvreader:
    #     print(row)

print('Election Results')
print('----------------------------------------')
print('Total Votes: ')
print('----------------------------------------')
# months = 
print('Charles Casper Stockham: ')
print('Diana DeGette: ')
print('Raymon Anthony Doane: $ ')
print('----------------------------------------')
print('Winner: ')
print('----------------------------------------')