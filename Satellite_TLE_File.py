#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Import required libraries
import os

class Satellite:
    def __init__(self, name, tle1, tle2):
        """Initializes a GPS satellite object with TLE data.
        :param name: Name of the satellite
        :param tle1: First line of TLE
        :param tle2: Second line of TLE"""
        self.name = name.strip()
        self.tle1 = tle1.strip()
        self.tle2 = tle2.strip()
        self.ssc_number = self.tle1.split()[1]  # Extract SSC Number
        self.epoch = self.tle1.split()[3]  # Extract reference epoch
        self.mean_anomaly = self.tle2.split()[6]  # Extract Mean Anomaly
        self.inclination = self.tle2.split()[2]  # Extract Inclination
        self.raan = self.tle2.split()[3]  # Extract Right Ascension of Ascending Node (RAAN)

    def __str__(self):
        """String representation of the Satellite object, formatted like your expected output."""
        return (f"\nSatellite name: {self.name}\n"
                f"SSC Number: {self.ssc_number}\n"
                f"Reference Epoch: {self.epoch}\n"
                f"Mean anomaly: {self.mean_anomaly}\n"
                f"Inclination: {self.inclination}°\n"
                f"RAAN: {self.raan}°\n"
                f"TLE data:\n{self.tle1}\n{self.tle2}\n")

def load_gps_tle(tle_file):
    """Reads the GPS TLE file and returns a list of Satellite objects.
    :param tle_file: Path to the TLE file
    :return: List of Satellite objects"""
    if not os.path.exists(tle_file):
        raise FileNotFoundError(f"Error: TLE file '{tle_file}' not found.")

    satellites = []
    with open(tle_file, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines) - 2:
        name = lines[i].strip()
        tle1 = lines[i + 1].strip()
        tle2 = lines[i + 2].strip()
        satellites.append(Satellite(name, tle1, tle2))
        i += 3  # Move to next satellite

    return satellites


# In[9]:


# Provide the correct file path
tlefile = 'gps-ops.txt'

try:
    # Load GPS satellites from the file
    gps_satellites = load_gps_tle(tlefile)

    # Print total satellites loaded
    print(f"Read in {len(gps_satellites)} satellites")

    # Print details of each satellite
    for sat in gps_satellites:
        print(sat)

except Exception as e:
    print(f"Error: {e}")


# In[15]:


for i, sat in enumerate(gps_satellites, start=1):
    print(f"{'-'*80}")
    print(f"Satellite {i}")
    print(str(sat))

