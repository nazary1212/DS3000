import pandas as pd

# Load the CSV
file_path = "co2_emissions_predictions_gradient_boosting_by_country_2020_2040.csv"  # Replace with your file path
data = pd.read_csv(file_path)

# Ensure Year column is integer
data['Year'] = data['Year'].astype(int)

# Filter data for years 2020 and 2040
data_2020 = data[data['Year'] == 2020]
data_2040 = data[data['Year'] == 2040]

# Merge the two datasets on Country to get emissions for both 2020 and 2040
merged_data = pd.merge(data_2020[['Country', 'Predicted CO2 Emissions (MtCO2)']],
                       data_2040[['Country', 'Predicted CO2 Emissions (MtCO2)']],
                       on='Country',
                       suffixes=('_2020', '_2040'))

# Calculate the total change in emissions between 2020 and 2040
merged_data['Emission Change (MtCO2)'] = merged_data['Predicted CO2 Emissions (MtCO2)_2040'] - merged_data['Predicted CO2 Emissions (MtCO2)_2020']

# Find the greatest carbon emitter in 2040
greatest_emitter_2040 = data_2040.loc[data_2040['Predicted CO2 Emissions (MtCO2)'].idxmax()]

# Print results
print("Total Change in Emissions (2020-2040):")
print(merged_data[['Country', 'Emission Change (MtCO2)']])

print("\nGreatest Carbon Emitter in 2040:")
print(f"Country: {greatest_emitter_2040['Country']}, Emissions: {greatest_emitter_2040['Predicted CO2 Emissions (MtCO2)']:.2f}")
