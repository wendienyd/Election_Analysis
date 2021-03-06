import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
   
   # To do: read and analyze the data here.
   #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)

    #Print each row in the CVS file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]
    
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
        

    #Determine the percentage of votes for each candidate by looping through the counts.
    #Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #Print the candidate name and percentage of votes.

        #To do: print out each candidate's name, vote count, and percentage of votes to terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determin winning vote and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"))

    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

        #print(winning_candidate_summary)


        # 3. Print the total votes.
        # print(total_votes)

        # #Print the candidate list.
        # print(candidate_options)

        # #Print the candidate vote dictionary.
        # print(candidate_votes)



        #Import the datetime class from the datetime module.
        # import datetime as dt
        # #Use the now() attribute on the datetime class to get the present time.
        # now = dt.datetime.now()

    #Use the open statement to open the file as a text file.
    # with open(file_to_save, "w") as txt_file:
    # #Write some data to the file

    #     #Write three counties to the file.
    #     txt_file.write("Arapahoe\nDenver\nJefferson")

    #Open the election results and read the file.
    # with open(file_to_load) as (election_data):