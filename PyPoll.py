import csv
import os

file_to_load = os.path.join('resources','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:

        total_votes += 1

        #Print the candidate name from each row.
        candidate_name = row[2]

        #Add candidates name to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Total votes per candidate and vote percentage
    for candidate in candidate_votes:

        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100

        print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        #  Winner of election
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate  
    
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    
print(winning_candidate_summary)



