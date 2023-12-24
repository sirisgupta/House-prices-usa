import csv
from datetime import datetime, timedelta

# Define the input and output file names
input_file = "MORTGAGE30US.csv"
output_file = "c2.csv"


# Read the original data from the CSV file
data = []
with open(input_file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        date_str, value = row
        data.append((datetime.strptime(date_str, '%d-%m-%Y'), float(value)))

# Create a list of all the first days of each month
date_range = []
current_date = data[0][0]
while current_date <= data[-1][0]:
    date_range.append(current_date)
    current_date = current_date.replace(day=1) + timedelta(days=32)
    current_date = current_date.replace(day=1)

# Interpolate data for the first day of each month
interpolated_data = []
data_index = 0
for date in date_range:
    while data_index < len(data) - 1 and data[data_index + 1][0] < date:
        data_index += 1
    if data_index < len(data) - 1:
        start_date, start_value = data[data_index]
        end_date, end_value = data[data_index + 1]
        days_between = (end_date - start_date).days
        days_to_interpolate = (date - start_date).days
        interpolated_value = start_value + (end_value - start_value) * days_to_interpolate / days_between
        interpolated_data.append((date, interpolated_value))
    else:
        interpolated_data.append((date, data[data_index][1]))

# Write the modified data to a new CSV file
with open(output_file, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    for date, value in interpolated_data:
        csv_writer.writerow([date.strftime('%d-%m-%Y'), value])
