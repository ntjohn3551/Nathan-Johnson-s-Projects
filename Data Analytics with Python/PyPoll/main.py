import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")


print("Election Results")
print("-------------------------")

voteCount = 0

charlesVotes = 0
dianaVotes = 0
raymonVotes = 0

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip the header
    csv_header = next(csv_file)
    
    # Read through each row of data after the header, counting votes
    for row in csv_reader:
        voteCount = voteCount + 1

        if(row[2]=="Charles Casper Stockham"):
            charlesVotes = charlesVotes + 1

        if(row[2]=="Diana DeGette"):
            dianaVotes = dianaVotes + 1

        if(row[2]=="Raymon Anthony Doane"):
            raymonVotes = raymonVotes + 1


# Determine the winner
if( (charlesVotes>dianaVotes) and (charlesVotes>raymonVotes) ):
    winner = "Charles Casper Stockham"

if( (dianaVotes>charlesVotes) and (dianaVotes>raymonVotes) ):
    winner = "Diana DeGette"

if( (raymonVotes>dianaVotes) and (raymonVotes>charlesVotes) ):
    winner = "Raymon Anthony Doane"


# Print all the necessary outputs
print("Total Votes: " + str(voteCount))
print("-------------------------")
print("Charles Casper Stockham: " + str(round(100*charlesVotes/(charlesVotes + dianaVotes + raymonVotes),3)) + "% (" + str(charlesVotes) + ")" )
print("Diana DeGette: " + str(round(100*dianaVotes/(charlesVotes + dianaVotes + raymonVotes),3)) + "% (" + str(dianaVotes) + ")" )
print("Raymon Anthony Doane: " + str(round(100*raymonVotes/(charlesVotes + dianaVotes + raymonVotes),3)) + "% (" + str(raymonVotes) + ")" )
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Export the output to a .txt file
textlines = [ "Election Results",
             "-------------------------",
             "Total Votes: " + str(voteCount), 
             "-------------------------",
             "Charles Casper Stockham: " + str(round(100*charlesVotes/(charlesVotes + dianaVotes + raymonVotes),3)) + "% (" + str(charlesVotes) + ")" , 
             "Diana DeGette: " + str(round(100*dianaVotes/(charlesVotes + dianaVotes + raymonVotes),3)) + "% (" + str(dianaVotes) + ")" ,
             "Raymon Anthony Doane: " + str(round(100*raymonVotes/(charlesVotes + dianaVotes + raymonVotes),3)) + "% (" + str(raymonVotes) + ")",
             "-------------------------",
             "Winner: " + winner,
             "-------------------------"
             ]

with open("Analysis/Election Results.txt", 'w') as f:
    for line in textlines:
        f.write(line)
        f.write('\n')