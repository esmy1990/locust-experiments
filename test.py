import csv
with open('example_stats.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    read_l = [{key:value for key, value in row.items() if key in ('Name', 'Average Response Time')}
              for row in reader]


with open('new.csv', 'w') as csvfile:
    fieldnames = read_l[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in read_l[0:]:
        writer.writerow(row)
