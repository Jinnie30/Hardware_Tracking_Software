#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
print(os.listdir())  # List files in the current directory


# In[2]:


#!jupyter nbconvert --to script Station_Parameters.ipynb
#!jupyter nbconvert --to script Satellite_TLE_File.ipynb
#!jupyter nbconvert --to script Tracking_Intervals_Inputs.ipynb
#!jupyter nbconvert --to script Link_Inputs.ipynb


# In[1]:


import sys
import os

# Ensure Python finds the local modules
sys.path.append(os.getcwd())

# Import all modules
from Station_Parameters import Station
from Satellite_TLE_File import Satellite
from Tracking_Intervals_Inputs import TrackingInterval
from Link_Inputs import LinkBudget

class FileIO:
    """
    Master class to load all input files (Station, Satellite TLE, Tracking Intervals, Link Budget).
    """

    def __init__(self):
        # File paths for the input data
        self.station_file = "station.dat"
        self.tle_url = "http://celestrak.org/NORAD/elements/gps-ops.txt"  # Live TLE Data
        self.tracking_file = "tracking_interval.dat"
        self.link_file = "link_inputs.dat"

        # Load all input data
        self.load_all_inputs()

    def load_all_inputs(self):
        """
        Reads and loads all input files.
        """
        print("\n📡 Loading Station Parameters...")
        self.station = Station(self.station_file)
        print(self.station)

        print("\n🛰️ Fetching Satellite TLE Data...")
        self.satellites = Satellite()
        print(self.satellites)

        print("\n⏳ Loading Tracking Interval...")
        self.tracking = TrackingInterval(self.tracking_file)
        print(self.tracking)

        print("\n📶 Loading Link Budget Inputs...")
        self.link_budget = LinkBudget(self.link_file)
        print(self.link_budget)

# Example Usage
if __name__ == "__main__":
    print("🚀 Initializing FileIO...")
    file_io = FileIO()


# In[9]:


from skyfield.api import Topos, load
from datetime import datetime

# Load the TLE data (replace this with actual TLE data from your file)
satellite = load.tle_file('gps-ops.txt')[0]  # Select the first satellite from TLE file

# Set the station location (latitude, longitude)
station = Topos(latitude_degrees=45.9555033333, longitude_degrees=281.9269597222)

# Set the observation time
timescale = load.timescale()
t = timescale.utc(2025, 3, 18, 12, 0)  # Set a specific date and time

# Compute the position of the satellite at time t
astrometric = satellite.at(t)

# Get the subpoint (latitude and longitude of the satellite's location on Earth)
subpoint = astrometric.subpoint()

# Now, we compute the azimuth and elevation from the station's location
alt, az, d = station.at(t).observe(satellite).apparent().altaz()

# Print the results
print(f"At time {t.utc_iso()}:")
print(f"Satellite Position: Latitude {subpoint.latitude.degrees}, Longitude {subpoint.longitude.degrees}")
print(f"Azimuth: {az.degrees}°, Elevation: {alt.degrees}°")


# In[ ]:




