import numpy as np

## Input parameters

# Supply voltage
Vcc = 10
# Upper limit of hysteresis threshold
VL = 4
# Lower limit of hysteresis threshold
Vh = 7
# Resistor Rx
Rx = 10000

# Makes parallel of 2 resistors
def parallel(R1, R2):
    return R1*R2/(R1+R2)

# Get solution

# Calculate Rh and Ry
Rh = VL/(Vh-VL)*Rx
Ry = VL/(Vcc-Vh)*Rx

print("Rh", Rh, "Ohm")
print("Ry", Ry, "Ohm")
print("Hysteresis window's width:", Vh-VL, "V")