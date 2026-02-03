# QUESTION 4
import pandas as pd
# Load the data set into a data frame
data_frame = pd.read_csv("student.csv")

# Filter students
filtered_data_frame = data_frame[(data_frame["studytime"] >= 3) & (data_frame["internet"] == 1) &
    (data_frame["absences"] <= 5) ]

# Save the filtered data to a new CSV
filtered_data_frame.to_csv("high_engagement.csv", index = False)

# Print the number of students and their average grade
count = len(filtered_data_frame)
average_grade = filtered_data_frame['grade'].mean()

print(f"Number of students: {count}")
print(f"Average grade of these students: {average_grade: .2f}")