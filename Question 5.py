#QUESTION 5
import pandas as pd
data_frame = pd.read_csv("student.csv")

# Create the grade band column
bins = [0, 9, 14, 20]
# 0-9 : Low, 10-14 : Medium, 15-50 : High
labels = ['Low', 'Medium', 'High']
data_frame['grade_band'] = pd.cut(data_frame['grade'], bins=bins, labels=labels, include_lowest = True)

# Create a grouped summary table
summary_table = data_frame.groupby('grade_band', observed = False).agg(
    number_of_students = ('grade', 'count'),
    average_absences=('absences', 'mean'),
    percentage_internet = ('internet', 'mean'))

# Convert the internet mean to a percentage
summary_table['percentage_internet'] = summary_table['percentage_internet'] * 100

# Save table
summary_table.to_csv("student_bands.csv")

# Print table
print(summary_table)
