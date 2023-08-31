import csv

# Function that takes file & column number as parameter and returns a list of all the values in that column
def return_column_csv(file, column_number):
    responses = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            responses.append(row[column_number])
    return responses