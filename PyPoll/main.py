import os
import csv

# Pull election data file

election_data = os.path.join("Resources", "election_data.csv")
with open(election_data, 'r') as csvfile:
    csvread = csv.reader(csvfile)

# Skips Header line
    
    next(csvread, None)
# Poll place holder for candidate name and vote
    poll = {}

    total_votes = 0
# Create cictionary list from 
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1

        else:
            poll[row[2]] = 1

# Create a list for candidates for vote count

candidates = []
num_votes = []




for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

# Creates vote percent list

vote_percent = []

for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

# Makes candidates, num_votes and vote_percent into tuples

new_data = list(zip(candidates, num_votes, vote_percent))

# Create list to put winners in

winner_list = []

for name in new_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# Makes winner list a string with the first entry

winner = winner_list[0]



# Will only run if there is a tie and if there are additional winners into a string
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]


output_file = os.path.join('election_results.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n----------------------- \nTotal Votes: ' + str(total_votes) + 
     '\n----------------------------\n')
    for entry in new_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'% (' + str(entry[1]) + ')\n')
    txtfile.writelines('--------------------------- \nWinner: ' + winner + '\n-------------------')

with open(output_file, 'r') as readfile:
    print(readfile.read())









