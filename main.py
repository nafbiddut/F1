from scripts.data_loader import load_session
from scripts.analysis import get_fastest_lap, average_lap_times, get_driver_laps
from scripts.visualization import plot_lap_times
from scripts.results import get_results

session = load_session(2024, "Monaco", "Race")

fastest_lap = get_fastest_lap(session)
print(f"Fastest Lap: {fastest_lap['Driver']} - {fastest_lap['LapTime']}")

print("\nAverage Lap Times:")
print(average_lap_times(session))

ver_laps = get_driver_laps(session, "VER")
print(ver_laps.head())

results = get_results(session)
print(results)

#plot_lap_times(session)
