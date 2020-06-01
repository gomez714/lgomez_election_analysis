import csv
import os

file_to_load = os.path.join('resources','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

#Candidates
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Counties
counties_participated = []
county_votes = {}
county_with_largest_turnout = ""
voter_turnout = 0
largest_voter_percentage = 0


with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        total_votes += 1

        # Candidates
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

        #Counties
        county_name = row[1]

        if county_name not in counties_participated:
            counties_participated.append(county_name)
            county_votes[county_name] = 0
        
        county_votes[county_name] += 1




with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # Total votes per county  and vote percentage
    for county in county_votes:

        votes = county_votes[county]
        vote_percentage = int(votes) / int(total_votes) * 100
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        print(county_results)
        txt_file.write(county_results)

        #  Largest voter turnout
        if (votes > voter_turnout) and (vote_percentage > largest_voter_percentage):
            
            voter_turnout = votes
            largest_voter_percentage = vote_percentage
            county_with_largest_turnout = county  
    
    #Summary for largest county turnout
    largest_turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {county_with_largest_turnout}\n"
        f"-------------------------\n")

    print(largest_turnout_summary)
    txt_file.write(largest_turnout_summary)



    # Total votes per candidate and vote percentage
    for candidate in candidate_votes:
        
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)


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
    txt_file.write(winning_candidate_summary)


