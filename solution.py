# Import the necessary libraries + functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read in our data
df = pd.read_csv("data.csv")

# Get our data columns as numpy arrays
x_label = "Distance to Center (arcminutes)"
y_label = "Rotational Velocity (km/sec)"
distance = df[x_label]
velocity = df[y_label]

# TODO: We'll complete the lab together!
# plt.scatter(distance, velocity)
# plt.show()

R_bulge = 1.6

# First, split up our data based on R_bulge
df_inner = df.loc[df[x_label] < R_bulge]
x_inner = df_inner[x_label]
y_inner = df_inner[y_label]
# print(x_inner)
# print(y_inner)

df_outer = df.loc[df[x_label] >= R_bulge]
x_outer = df_outer[x_label]
y_outer = df_outer[y_label]
# print(x_outer)
# print(y_outer)

# Next, fit the data
def Vr_inner(r, A):
    return A*r

popt_inner, pcov_inner = curve_fit(Vr_inner, 
x_inner, 
y_inner)
print(popt_inner, pcov_inner)

# Now, use A to calculate velocity for r >= R_bulge
def Vr_outer(r, A):
    return A * R_bulge**(3/2) / (r**0.5)

inner_linspace = np.linspace(x_inner.min(), R_bulge, 100)
outer_linspace = np.linspace(R_bulge, x_outer.max(), 
100)

plt.plot(inner_linspace, Vr_inner(inner_linspace, popt_inner))
plt.scatter(x_inner, y_inner)
plt.plot(outer_linspace, Vr_outer(outer_linspace, 
popt_inner))
plt.scatter(x_outer, y_outer)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()
