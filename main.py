# Import the necessary libraries + functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read in our data
df = pd.read_csv("data.csv")

# Get our data columns as numpy arrays
distance = df["Distance to Center (arcminutes)"]
velocity = df["Rotational Velocity (km/sec)"]

print(df)

# TODO: We'll complete the lab together!