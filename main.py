# Import the necessary libraries + functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read in our data
data = pd.read_csv("data.csv")

# Get our data columns as numpy arrays
x_data = data["Distance to Center (arcminutes)"]
y_data = data["Rotational Velocity (km/sec)"]

# TODO: We'll complete the lab together!