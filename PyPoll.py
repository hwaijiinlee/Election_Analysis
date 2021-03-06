# Add dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt") 

# Initialize total vote counter
total_votes = 0

# Initialize candidate list
candidate_options = []

# Initialize empty dictionary of candidates' vote count
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:    
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)    

    # Print each row in the CSV file
    for row in file_reader:        

        # Add to the total vote count
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]

        # Add unique candidate name to candidate options list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking candidates' vote count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1   

# Save the results to election_analysis file
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        
    print(election_results, end="")

    # Save final vote count to the text file
    txt_file.write(election_results)    

# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")    
            
        # Print candidate name and percentage of votes
        print(candidate_results)
        # Save candidate results to txt file
        txt_file.write(candidate_results)
        
        # Determine winning vote count and candidate
        # Determine if votes are greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
        
    # Print winning candidate's statistics
    winning_candidate_summary = (
            f"----------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage: .1f}%\n"
            f"-----------------------\n")
        
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

