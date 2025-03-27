import fastf1
print("FastF1 is installed and working!")

session = fastf1.get_session(2024, 'Monza', 'Race')
session.load()

df = session.laps



print(df)