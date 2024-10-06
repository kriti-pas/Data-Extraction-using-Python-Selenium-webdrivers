import pandas as pd
import numpy as np
import csv

from pathlib import Path

df = pd.read_csv("C:\\Users\\LOHITHA614\\Desktop\\booking_2024_update.csv")
df['Sleeper'] = df['Bus Name']
df['Seater'] = df['Bus Name']
df['AC'] = df['Bus Name']
df['NON-AC'] = df['Bus Name']
for i in range(len(df['Bus Name'])):
    df['Sleeper'][i] = "yes" if "Sleeper" in df['Bus Name'][i] else "no"
    df['Seater'][i] = "yes" if "Seater" in df['Bus Name'][i] else "no"
    df['AC'][i] = "yes" if "AC" in df['Bus Name'][i] else "no"
    df['NON-AC'][i] = "yes" if "NON-AC" in df['Bus Name'][i] else "no"
# df = pd.DataFrame(mobile_details)
filepath = Path('booking.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
print(df)
