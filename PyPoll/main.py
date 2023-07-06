# Author: Ashley Paillet
# Module 3 Challenge, PyPoll
# /Users/ashleypaillet/Desktop/git_HUB/03-python-challenge/python-challenge/PyPoll
# election_data = '../Resources/election_data.csv'

import os
import csv
election_csv = os.path.join('Resources', 'election_data.csv')

with open(election_csv, encoding='UTF-8') as csvfile:
    election_reader = csv.reader(csvfile, delimiter=',')
    election_header = next(election_reader)
    #
    ballots = {}
    sum_ballot = 0
    #
    most_votes = 0
    winner = 0
    #
    for row in election_reader:
        sum_ballot += 1
        if row[2] in ballots:
            ballots[row[2]] += 1
        else:
            ballots[row[2]] = 1
    print('Election Results')
    print('----------------------------------------')
    print(f'Total Votes: {sum_ballot}')
    print('----------------------------------------')
    for runners, votes in ballots.items():
        print(f'{runners} : {round(((votes/sum_ballot) * 100), 3)}% ({votes})')
        if votes > most_votes:
            most_votes = votes
            winner = runners
    print('----------------------------------------')
    print(f'Winner: {winner}')
    print('----------------------------------------')            
    #
    export_py_bank = os.path.join('analysis', 'py_poll.txt')
    with open(export_py_bank, 'w') as f:
        f.write('Author: Ashley Paillet\n')
        f.write('----------------------------------------\n')
        f.write('Election Results\n')
        f.write('----------------------------------------\n')
        f.write(f'Total Votes: {sum_ballot} \n')
        f.write('----------------------------------------\n')
        for runners, votes in ballots.items():
            f.write(f'{runners} : {round(((votes/sum_ballot) * 100), 3)}% ({votes})\n')
        f.write('----------------------------------------\n')
        if votes > most_votes:
            most_votes = votes
            winner = runners
        f.write(f'Winner: {winner}\n')
        f.write('----------------------------------------\n')