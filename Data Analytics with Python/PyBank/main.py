import os
import csv

financial_csv = os.path.join("Resources", "budget_data.csv")


print("Financial Analysis")
print("----------------------------")

months = 0
total = 0

totalChange = 0

evenRow = "empty"
oddRow = "empty"

greatestIncrease = 0
greatestDecrease = 0

# In case profits were completely stable
greatestIncreaseMonth = "profits did not change"
greatestDecreaseMonth = "profits did not change"


with open(financial_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip the header
    csv_header = next(csv_file)
    
    # Read through each row of data after the header
    for row in csv_reader:

            # For every row, increase the month count
            months = months + 1
            total = total + int(row[1])

            # For the first row, assign the oddRow value
            if ((oddRow == "empty") and (evenRow == "empty") ):
                oddRow = int(row[1])

            # If the oddRow isnt empty, assign the even row and evaluate the change
            if ( (not(oddRow == "empty")) and (evenRow == "empty") ):
                evenRow = int(row[1])
                totalChange = totalChange + (evenRow - oddRow)

                # If change is larger or smaller than what is currently the greatest increase or decrease, record this month's change and month date
                if((evenRow - oddRow) > greatestIncrease):
                    greatestIncrease = (evenRow - oddRow)
                    greatestIncreaseMonth = row[0]

                if((evenRow - oddRow) < greatestDecrease):
                    greatestDecrease = (evenRow - oddRow)
                    greatestDecreaseMonth = row[0]

                # Reset the odd row
                oddRow = "empty"

            # If the evenRow isnt empty, assign the odd row and evaluate the change
            if ((oddRow == "empty") and (not(evenRow == "empty")) ):
                oddRow = int(row[1])
                totalChange = totalChange + (oddRow - evenRow)
                
                # If change is larger or smaller than what is currently the greatest increase or decrease, record this month's change and month date
                if((evenRow - oddRow) > greatestIncrease):
                    greatestIncrease = (evenRow - oddRow)
                    greatestIncreaseMonth = row[0]

                if((evenRow - oddRow) < greatestDecrease):
                    greatestDecrease = (evenRow - oddRow)
                    greatestDecreaseMonth = row[0]
                
                # Reset the even row
                evenRow = "empty"


# Print all the necessary outputs
print("Total Months: " + str(months))
print("Total: $" + str(total))
print("Average Change: $" + str( round( (totalChange/(months-1)), 2) ) )
print("Greatest Increase in Profits: " + greatestIncreaseMonth + " ($" + str(round(greatestIncrease,2)) + ")" )
print("Greatest Decrease in Profits: " + greatestDecreaseMonth + " ($" + str(round(greatestDecrease,2)) + ")" )

# Export the output to a .txt file
textlines = [ "Financial Analysis", "----------------------------", 
              "Total Months: " + str(months), 
              "Total: $" + str(total), 
              "Average Change: $" + str( round( (totalChange/(months-1)), 2) ), 
              "Greatest Increase in Profits: " + greatestIncreaseMonth + " ($" + str(round(greatestIncrease,2)) + ")" , 
              "Greatest Decrease in Profits: " + greatestDecreaseMonth + " ($" + str(round(greatestDecrease,2)) + ")" 
              ]

with open("Analysis/Financial Analysis.txt","w") as f:
    for line in textlines:
        f.write(line)
        f.write('\n')