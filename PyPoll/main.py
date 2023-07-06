# Author: Ashley Paillet
# Module 3 Challenge, PyPoll
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
    print('Charles Casper Stockham: ')
    print('Diana DeGette: ')
    print('Raymon Anthony Doane: $ ')
    print('----------------------------------------')
    print('Winner: ')
    print('----------------------------------------')
    
    export_py_bank = os.path.join('analysis', 'py_poll.txt')
    with open(export_py_bank, 'w') as f:
        f.write('Author: Ashley Paillet\n')
        f.write('----------------------------------------\n')
        f.write('Election Results\n')
        f.write('----------------------------------------\n')
        f.write('Total Votes: \n')
        f.write('----------------------------------------\n')
        f.write('Charles Casper Stockham: \n')
        f.write('Diana DeGette: \n')
        f.write('Raymon Anthony Doane: $ \n')
        f.write('----------------------------------------\n')
        f.write('Winner: \n')
        f.write('----------------------------------------\n')