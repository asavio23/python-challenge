import os
import csv

myfile = os.path.join('Resources','budget_data.csv')

#read csv 
with open (myfile) as csv_file:
    csvreader = csv.reader(csv_file, delimiter =",")
    csv_header = next(csvreader)
    
    #Values 
    totalmonths = 0
    prev_rev = 0
    month_of_change = []
    rev_change_list = []
    greatest_inc_month = [""]
    greatest_inc_rev = int(1)
    greatest_dec_month = [""]
    greatest_dec_rev = int(1)
    total_sum = 0 

    for row in csvreader:

    #track totals 
        totalmonths = totalmonths + 1 
        total_sum = total_sum + int(row[1])
    #Trake the revenue change 
        if (totalmonths > 1):
            rev_change = int(row[1]) - prev_rev 
            rev_change_list = rev_change_list + [rev_change]
        #calculate greatest_inc 
            if(rev_change > greatest_inc_rev): 
                greatest_inc_month = row[0]
                greatest_inc_rev = rev_change
        #calculate greatest_dec 
            if(rev_change < greatest_dec_rev): 
                greatest_dec_month = row[0]
                greatest_dec_rev = rev_change
        prev_rev = int(row[1]) 
        month_of_change = month_of_change + [row[0]] 

#calculate average rev change 
rev_average = sum(rev_change_list) / len(rev_change_list)

#Generate Output sum 
print_statement = str( 
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {totalmonths}\n"
    f"Total: ${total_sum}\n"
    f"Average Change: ${rev_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc_rev})\n"
    f"Greatest Increase in Profits: {greatest_dec_month} (${greatest_dec_rev})\n"
)
print(print_statement)


#Print results to text file 
output = os.path.join ('Analysis', 'budget_summary.txt')
file = open(output, "w")
file.write(print_statement)
