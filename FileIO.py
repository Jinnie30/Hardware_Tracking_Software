#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
print(os.listdir())  # List files in the current directory


# In[5]:


#!jupyter nbconvert --to script Station_Parameters.ipynb
get_ipython().system('jupyter nbconvert --to script Satellite_TLE_File.ipynb')
#!jupyter nbconvert --to script Tracking_Intervals_Inputs.ipynb
#!jupyter nbconvert --to script Link_Inputs.ipynb


# In[17]:


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
        Reads and loads all input files, including station parameters, satellite TLEs, 
        tracking intervals, and link budgets.
        """
    
        print("\n Loading Station Parameters...")
        self.station = Station(self.station_file)
        print(self.station)
    
        #print("\n Fetching Satellite Data...")
    
        # Reading the TLE file
        tlefile=r'C:\Users\jinni\Hardware_Tracking_Software\gps-ops.txt'
        with open(tlefile, 'r') as TLEfile:
         lines = TLEfile.readlines()
    
        self.satellites = []  # Store multiple satellites
        i = 0
        while i < len(lines) - 2:  # Process each satellite (3 lines per entry)
            name = lines[i].strip()   # Satellite name
            tle1 = lines[i + 1].strip()  # TLE Line 1
            tle2 = lines[i + 2].strip()  # TLE Line 2
            self.satellites.append(Satellite(name, tle1, tle2))  
            i += 3  # Move to the next satellite
    
        print(f"Loaded {len(self.satellites)} satellites.")
        print(self.satellites)
    
        print("\n Loading Tracking Interval...")
        self.tracking = TrackingInterval(self.tracking_file)
        print(self.tracking)
    
        print("\n Loading Link Budget Inputs...")
        self.link_budget = LinkBudget(self.link_file)
        print(self.link_budget)


# Example Usage
if __name__ == "__main__":
    print("🚀 Initializing FileIO...")
    file_io = FileIO()


# In[ ]:




