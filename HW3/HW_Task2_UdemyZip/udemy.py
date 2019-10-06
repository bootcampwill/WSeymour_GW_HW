import os
import csv

udemy_csv = os.path.join("web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        title.append(row[1])

        # Add price
        price.append(row[4])

        # Add number of subscribers
        subscribers.append(row[5])
        subscribers = [int(s) for s in subscribers]
        # Add amount of reviews
        reviews.append(row[6])
        reviews = [int(i) for i in reviews]
        
        #add length
        length.append(row[9])
        
        # Determine percent of review left to 2 decimal places
        review_percent = [reviews/subscribers for subscribers, reviews in zip(subscribers, reviews)]
        review_percent = [round(float(p)*100,2) for p in review_percent]
        
        # Get length of the course to just a number
        time = [unit for time in length for unit in time.split(' ')]
        
        for unit in time:
            if unit == "hours":
                unit - 1 = (unit - 1)*60


# Zip lists together
output = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    writer.writerows(output)


