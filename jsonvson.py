import pandas as pd

# Load CSV into a DataFrame
df = pd.read_csv('booking.csv')

# Convert DataFrame to JSON
json_data = df.to_json(orient='records', indent=2)

# Save JSON data to a file
with open('dataset.json', 'w') as json_file:
    json_file.write(json_data)
