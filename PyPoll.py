import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
   
   # To do: read and analyze the data here.
   #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    print(headers)



#Import the datetime class from the datetime module.
# import datetime as dt
# #Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()

#Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
#Write some data to the file

    #Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")

#Open the election results and read the file.
# with open(file_to_load) as (election_data):