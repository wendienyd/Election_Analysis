# Python_Election_Analysis

## Overview of Election Audit

A Colorado Board of Elections employee has requested a minimun of 5 tasks to complete a local congressional election audit. These tasks are the following:

1. Calculating the total number of votes cast.
2. Getting a complete list of candidates who received votes.
3. Calculating the total number of votes each candidate received.
4. Calculating the percentage of votes each candidate won.
5. Determining the winner of the election based on popular vote.

The election commission also asked for some additional data to complete the audit:

- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

### Resources

- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.68.1

## Election-Audit Results:

The analysis of the election show that:
- There were a total of 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham who received 23% of the vote with (85,213) number of votes.
    - Diana DeGette received who 73.8% of the vote with (272,892) number of votes.
    - Raymon Anthony Doane who received 3.1% of the vote with (11,606) number of votes
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and (272,892) number of votes.
    
 Additional data results:
- County Jefferson:
    - The total voter count was (38,855)
    - percentage rate was 10.5%
- County Denver:
    - The total voter count was (306,055)
    - percentage rate was 82.8%
- County Arapahoe:
    - The total voter count was (24,801)
    - percentage rate was 6.7%
- The county with the largest turnout: Denver

## Election-Audit Summary:

The python code provided is "robut" and can be used for any state wide election.

    1. The statements used for counties and candidates were not hard-wired to a specific person or place.
       Like when a candidate name was added to the candidate list, it typed:   
            candidate_options.append(candidate_name)
    
    2. The methods we used to calculate results can be reused with other elections.
       Like when the counties percentage of votes was calculated:
            county_percentage = (county_vote) / float(total_votes) * 100

    

