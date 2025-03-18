#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re
from datetime import datetime

class TrackingInterval:
    """
    Reads tracking interval parameters from tracking_interval.dat.
    """
    def __init__(self, filename):
        self.start_time = None
        self.duration = 0
        self.time_step = 0
        self.read_tracking_file(filename)

    def read_tracking_file(self, filename):
        """
        Reads tracking parameters from a given file, ignoring comments.
        """
        try:
            with open(filename, "r") as file:
                # Remove comments, strip whitespace, and filter empty lines
                lines = [re.sub(r"#.*", "", line).strip() for line in file.readlines()]
                lines = [line for line in lines if line]  # Remove empty lines

                print("📂 Reading tracking_interval.dat...")  # Debugging

                # Read start time and convert it to a datetime object
                self.start_time = datetime.strptime(lines[0], "%Y-%m-%d %H:%M:%S")
                
                # Read duration and time step
                self.duration = int(lines[1])
                self.time_step = int(lines[2])

        except FileNotFoundError:
            print(f"❌ Error: {filename} not found.")
        except ValueError as e:
            print(f"❌ Error reading {filename}: {e} (Check for incorrect values)")
        except Exception as e:
            print(f"❌ Unexpected error reading {filename}: {e}")

    def __str__(self):
        return (f"⏳ Tracking Interval:\n"
                f"   🕒 Start Time: {self.start_time} UTC\n"
                f"   ⏳ Duration: {self.duration} seconds ({self.duration / 60} min)\n"
                f"   ⏲️ Time Step: {self.time_step} seconds ({self.time_step / 60} min)")

# Example Usage
if __name__ == "__main__":
    tracking = TrackingInterval("tracking_interval.dat")
    print(tracking)


# In[ ]:




