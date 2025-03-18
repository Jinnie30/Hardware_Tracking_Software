#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests 
class SatelliteTLE:
    """
    Fetches and stores satellite TLE data from Celestrak.
    """
    TLE_URL = "http://celestrak.org/NORAD/elements/gps-ops.txt"

    def __init__(self):
        self.tle_data = []
        self.fetch_tle_data()

    def fetch_tle_data(self):
        """
        Fetches the latest GPS TLE data from Celestrak.
        """
        try:
            response = requests.get(self.TLE_URL)
            response.raise_for_status()
            lines = response.text.strip().split("\n")

            for i in range(0, len(lines), 3):
                if i + 2 < len(lines):
                    self.tle_data.append((lines[i], lines[i+1], lines[i+2]))

        except requests.RequestException as e:
            print(f"Error fetching TLE data: {e}")
    def list_tles(self):
            """
            Prints the fetched TLEs in a readable format.
            """
            if not self.tle_data:
                print("No TLE data available.")
                return
    
            print(f"Fetched {len(self.tle_data)} satellites from Celestrak:\n")
            for sat_name, line1, line2 in self.tle_data:
                print(f"📡 Satellite: {sat_name}")
                print(f"   {line1}")
                print(f"   {line2}\n")
    def __str__(self):
        return f"Fetched {len(self.tle_data)} satellites from Celestrak."


# In[16]:


tle = SatelliteTLE()
print(tle)


# In[17]:


if __name__ == "__main__":
    tle = SatelliteTLE()
    print(tle)  # Prints summary
    tle.list_tles()  # Prints all fetched TLEs


# In[11]:


#from FileIO import SatelliteTLE


# In[ ]:




