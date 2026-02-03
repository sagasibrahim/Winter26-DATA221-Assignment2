#QUESTION 6
import pandas as pd
import numpy as np
# Load crime dataset
crime_data_frame = pd.read_csv("crime.csv")

# Create risk column
crime_data_frame['risk'] = np.where(crime_data_frame['ViolentCrimesPerPop'] >= 0.50, "HighCrime", "LowCrime")

# Group by risk and calculate mean unemployment
risk_summary = crime_data_frame.groupby('risk')['PctUnemployed'].mean()

# Print
print("Average Unemployment Rate by Crime Risk:")
print("-" * 40)
print(f"HighCrime: {risk_summary['HighCrime']:.4f}")
print(f"LowCrime:  {risk_summary['LowCrime']:.4f}")