import fastf1
import pandas as pd
print("FastF1 is installed and working!")

#Load the session
session = fastf1.get_session(2024, 'Monza', 'Race')
session.load()

df = session.laps



#print(df)

# Create a DataFrame to store drivers and their average lap times
driver_avg_times = []

# Loop through each unique driver in the session data
for driver in session.laps['Driver'].unique():
    # Get all laps for the current driver
    driver_laps = session.laps.pick_driver(driver)

    # Calculate the average lap time (excluding invalid laps)
    avg_lap_time = driver_laps['LapTime'].mean()

    # Store driver and their average lap time
    driver_avg_times.append({"Driver": driver, "AverageLapTime": avg_lap_time})

# Convert list to DataFrame for sorting
df_avg_times = pd.DataFrame(driver_avg_times)

# Sort the drivers by average lap time (ascending order, fastest first)
df_avg_times = df_avg_times.sort_values(by="AverageLapTime").reset_index(drop=True)

# Display the results
print(df_avg_times)