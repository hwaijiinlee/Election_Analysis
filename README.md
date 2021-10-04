# Election Analysis
## Overview
The project is undertaken to determine the winner of the election in Colorado out of three counties - Arapahoe, Denver and Jefferson. We are to determine the vote count of each candidate and the percentage of total votes they received to evaluate the winner. We are also to determine which county had the largest voter turnout by vote count and percentage of total votes cast.

## Election Audit Results
[Summary of Election Results](https://github.com/hwaijiinlee/Election_Analysis/blob/main/analysis/election_analysis.txt)
### Audit by County
A total of 369,711 votes were cast in Arapahoe, Denver and Jefferson counties. Denver had the largest voter turnout with 306,055 votes or 82.8% of total votes cast of the three counties combined, followed by Jefferson county with 38,855 or 10.5% of total votes, then Arapahoe with 24,801 votes or 6.7% of total votes.

### Audit by Candidate
Diana DeGette won the election with an overwhelming majority of 73.8% of total votes cast or 272,892 votes while Charles Casper Stockham received 23% of the total votes or 85,213 votes. Raymon Anthony Doane only managed to garner 3.1% of total votes or 11,606 votes.

## Election Audit Summary
The Python script used to audit the election results can be modified to handle election at city-level as well. 
### Use for City or Township Level Elections
In Mayoral elections for a city, we can re-use the script by removing the sections as they relate to county vote counts and the script would then only determine the winning Mayoral candidate for that city.

In city elections whereby there are several Propositions to be voted on for example, sales tax increase, legalization of recreational marijuana, and removal of dog breed specific legislation, we can remove the sections where they relate to county vote counts, replace the candidate list and library with each Proposition's list and library, and replicate the calculation just like they are currently done to determine the number and percentage of each Proposition's yays and nays and subsequently, the winning option of each measure.

Here is an example of the modified code: [Multiple Proposition Audit](https://github.com/hwaijiinlee/Election_Analysis/blob/main/multiple_prop.py)
