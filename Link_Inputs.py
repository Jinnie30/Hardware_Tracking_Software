#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

class LinkBudget:
    """
    Reads link budget parameters from link_inputs.dat.
    """
    def __init__(self, filename):
        self.frequency = 0.0  # MHz
        self.antenna_efficiency = 0.0  # η
        self.antenna_diameter = 0.0  # m
        self.bandwidth = 0.0  # MHz
        self.receiver_gain = 0.0  # dB
        self.receiver_noise_temp = 0.0  # deg K
        self.read_link_file(filename)

    def read_link_file(self, filename):
        """
        Reads link budget parameters from a given file, ignoring comments.
        """
        try:
            with open(filename, "r") as file:
                # Remove comments, strip whitespace, and filter empty lines
                lines = [re.sub(r"#.*", "", line).strip() for line in file.readlines()]
                lines = [line for line in lines if line]  # Remove empty lines

                print("📂 Reading link_inputs.dat...")  # Debugging

                # Read values from file
                self.frequency = float(lines[0])  # Frequency (MHz)
                self.antenna_efficiency = float(lines[1])  # Antenna Efficiency (η)
                self.antenna_diameter = float(lines[2])  # Antenna Diameter (m)
                self.bandwidth = float(lines[3])  # Bandwidth (MHz)
                self.receiver_gain = float(lines[4])  # Receiver Gain (dB)
                self.receiver_noise_temp = float(lines[5])  # Receiver Noise Temperature (K)

        except FileNotFoundError:
            print(f"❌ Error: {filename} not found.")
        except ValueError as e:
            print(f"❌ Error reading {filename}: {e} (Check for incorrect values)")
        except Exception as e:
            print(f"❌ Unexpected error reading {filename}: {e}")

    def __str__(self):
        return (f"📡 Link Budget Parameters:\n"
                f"   📶 Frequency: {self.frequency} MHz\n"
                f"   📡 Antenna Efficiency: {self.antenna_efficiency}\n"
                f"   📡 Antenna Diameter: {self.antenna_diameter} m\n"
                f"   🔊 Bandwidth: {self.bandwidth} MHz\n"
                f"   📡 Receiver Gain: {self.receiver_gain} dB\n"
                f"   🔥 Receiver Noise Temperature: {self.receiver_noise_temp} K")

# Example Usage
if __name__ == "__main__":
    link_budget = LinkBudget("link_inputs.dat")
    print(link_budget)


# In[ ]:




