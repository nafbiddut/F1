import pandas as pd

def get_fastest_lap(session):
    return session.laps.pick_fastest()

def average_lap_times(session):
    return session.laps.groupby("Driver")["LapTime"].mean().sort_values()

def get_driver_laps(session, driver_code):
    laps = session.laps.pick_driver(driver_code)
    return laps[["LapNumber", "LapTime", "Sector1Time", "Sector2Time", "Sector3Time"]]