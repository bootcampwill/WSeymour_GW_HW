# -*- coding: UTF-8 -*-
"""PyPoll Homework Solution."""

# Incorporated the csv module
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = []
candidate_final = []

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row...
    for row in reader:

        # Run the loader animation, Seriously, Dart?
       # print(". ", end=""),

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name) 

            # And begin tracking that candidate's voter count
            candidate_votes.append(1)

                
        # Then add a vote to that candidate's count
        else:
            candidate_index=candidate_options.index(candidate_name)
            candidate_votes[candidate_index] += 1

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    print(f'Total Votes: {total_votes}\n*****************\nCandidate Vote Tallies\n')

    # Save the final vote count to the text file
    file = open(file_to_output,"w")
    file.write(f'Total Votes: {total_votes}\n*****************\nCandidate Vote Tallies\n')
    file.close()           
    # Determine the winner by looping through the counts
    pct_list = []
    for candidate in range(len(candidate_votes)):

        # Retrieve vote count and percentage
        #votes = candidate_votes.get(candidate)
        vote_percentage = round(candidate_votes[candidate] / float(total_votes) * 100)
        pct_list.append(vote_percentage)
        # Determine winning vote count and candidate
        winning_count = max(candidate_votes)
        winning_index = candidate_votes.index(winning_count)
        winning_candidate = candidate_options[winning_index]
        winning_pct = pct_list[winning_index]
        
        # Print each candidate's voter count and percentage (to terminal)
        print(f'{candidate_options[candidate]}: {candidate_votes[candidate]}, {pct_list[candidate]}%')
        
        #save as text
        file = open(file_to_output,"a")

        file.write(f'{candidate_options[candidate]}: {candidate_votes[candidate]}, {pct_list[candidate]}%\n')
        file.close()                
        # Print the winning candidate (to terminal)
    print(f'************\nAND THE WINNER IS:\n{winning_candidate}!')
    
    #add winner
    file = open(file_to_output, "a")
    file.write(f'************\nAND THE WINNER IS:\n{winning_candidate}!')
    file.close()
    
