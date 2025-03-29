import matplotlib.pyplot as plt

def plot_lap_times(session):
    for driver in session.laps["Driver"].unique():
        laps = session.laps.pick_driver(driver)
        plt.plot(laps.index, laps["LapTime"], label=driver)
    
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (s)")
    plt.title("Driver Lap Times")
    plt.legend()
    plt.grid()
    plt.show()
