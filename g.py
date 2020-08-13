from csv import reader

with open('new.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    flag = 0
    for row in csv_reader:
        for field in row[1:]:
            #try:
                field = float(field)
                if (field >= 150):
                    flag = 1
                    break
print(flag)
