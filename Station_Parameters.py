#!/usr/bin/env python
# coding: utf-8

# In[17]:


import re  # For cleaning comments

class Station:
    """
    Handles station parameters from station.dat file.
    """
    def __init__(self, filename):
        self.name = ""
        self.latitude = 0.0
        self.longitude = 0.0
        self.altitude = 0.0
        self.utc_offset = 0.0
        self.diameter = 0.0
        self.focal_ratio = 0.0
        self.focal_length = 0.0
        self.surface_accuracy_solid = 0.0
        self.surface_accuracy_mesh = 0.0
        self.beamwidth = 0.0
        self.az_speed_max = 0.0
        self.el_speed_max = 0.0
        self.el_min_limit = 0.0
        self.el_max_limit = 0.0
        self.az_el_limits = []
        self.read_station_file(filename)

    def read_station_file(self, filename):
        """
        Reads station parameters from a given file, handling comments and multi-value lines.
        """
        try:
            with open(filename, "r") as file:
                # Remove comments and strip whitespace
                lines = [re.sub(r"#.*", "", line).strip().replace(",", "") for line in file.readlines()]
                
                self.name = lines[0]
                self.latitude = float(lines[1])
                self.longitude = float(lines[2])
                self.altitude = float(lines[3])
                self.utc_offset = float(lines[4])
                self.diameter = float(lines[5])
                self.focal_ratio = float(lines[6])
                self.focal_length = float(lines[7])
                self.surface_accuracy_solid = float(lines[8])
                self.surface_accuracy_mesh = float(lines[9])
                self.beamwidth = float(lines[10])
                self.az_speed_max = float(lines[11])
                self.el_speed_max = float(lines[12])
                self.el_min_limit = float(lines[13])
                self.el_max_limit = float(lines[14])

                num_limits = int(lines[15])

                for i in range(num_limits):
                    parts = lines[16 + i].strip().split()  # Explicitly split by spaces
                    if len(parts) == 3:
                        az, min_el, max_el = map(float, parts)  # Convert each part to float
                        self.az_el_limits.append((az, min_el, max_el))
                    else:
                        print(f"⚠ Warning: Incorrect format in line {16 + i + 1}: '{lines[16 + i]}'")

        except FileNotFoundError:
            print(f"❌ Error: {filename} not found.")
        except ValueError as e:
            print(f"❌ Error reading {filename}: {e} (Check for incorrect values)")
        except Exception as e:
            print(f"❌ Unexpected error reading {filename}: {e}")

    def __str__(self):
        az_el_str = "\n".join([f"Azimuth: {az}°, Min Elev: {min_el}°, Max Elev: {max_el}°"
                               for az, min_el, max_el in self.az_el_limits])

        return (f"📡 Station: {self.name}\n"
                f"🌍 Latitude: {self.latitude}°, Longitude: {self.longitude}°, Altitude: {self.altitude} m\n"
                f"⏳ UTC Offset: {self.utc_offset} hrs\n"
                f"🔭 Diameter: {self.diameter} m, Focal Ratio: {self.focal_ratio}, Focal Length: {self.focal_length} m\n"
                f"🎯 Surface Accuracy: {self.surface_accuracy_solid} cm (solid), {self.surface_accuracy_mesh} cm (mesh)\n"
                f"📡 Beamwidth: {self.beamwidth} arcmin\n"
                f"🔄 AZ Speed Max: {self.az_speed_max} deg/min, EL Speed Max: {self.el_speed_max} deg/min\n"
                f"🔼 EL Min Limit: {self.el_min_limit}°, EL Max Limit: {self.el_max_limit}°\n"
                f"🗺️ Azimuth/Elevation Limits:\n{az_el_str}")

# Example Usage
if __name__ == "__main__":
    station = Station("station.dat")
    print(station)


# In[ ]:




