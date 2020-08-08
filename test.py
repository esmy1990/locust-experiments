import csv
with open('example_stats.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("Name Average Response Time")
 print("---------------------------------")
 for row in data:
   print(row['Name'], row['Average Response Time'])
