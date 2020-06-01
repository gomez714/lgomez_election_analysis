import csv
import os

file_to_load = os.path.join('resources','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)
    print(headers)

# What script needs to do (Data we need retrieved)
#1. Total number of votes
# 2. Complete list of candidates who received votes
# 3. Total number of votes for each candidate
# 4. Who got the most votes (winner)


