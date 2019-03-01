import numpy as np

#---------------------------------------------------------------------------------------------------
# Series RLC circuit:

# Output: capacitor voltage

# Writing a KVL to the loop and substituting the characteristic equation of the capacitor, we get
# d^2(Vc)/dt^2 + R/L dVc/dt + Vc/(LC) = Vsource

# and the following characteristic equation of the natural response
# s^2 + 2 alpha s + w0^2 = 0

# The solution is of the form (Vp = particular solution)
# Vc(t) = Vt + Vp

print("---------------------------Series RLC circuit----------------------------------------")

R = 5
L = 30 * 10**(-3)
C = 100 * 10**(-6)

# Natural frequency [Rad/s]
w0 = 1/np.sqrt(L*C)
print("Natural frequency:", w0, "[rad/s]")
# Damping rate
alpha = R/(2*L)
print("Damping rate:", alpha, "[1/s]")
# Time to zero (4 tau)
print("Time before exponential term goes to zero:", 4 * 1/alpha, "[s]")
# Damping factor
damping_factor = alpha / w0

# The poles are given by
if alpha == w0 : # or if damping_factor = 1
    print("Critically damped system: poles are real and s1 = s2")
    s1 = -alpha
    s2 = -alpha
    print("s1:", s1)
    print("s2:", s2)
elif alpha > w0: # or if damping_factor > 1
    print("Over damped system: poles are real but s1 != s2")
    s1 = - alpha + np.sqrt(alpha**2 - w0**2) 
    s2 = - alpha - np.sqrt(alpha**2 - w0**2)
    print("s1:", s1)
    print("s2:", s2)
else: # or if damping_factor < 1
    print("Under damped system: poles are complex conjugate")
    s1 = -alpha + 1j * np.sqrt(-alpha**2 + w0**2) 
    s2 = -alpha - 1j * np.sqrt(-alpha**2 + w0**2)
    # Csi = damping factor
    damping_factor = 0.5 * R * np.sqrt(C/L) # or alpha/w0
    # I can write the poles also as s1,2 = -alpha +- 1j*w0*np.sqrt(1-damping_factor**2) = -alpha +- 1j*wd
    wd = w0 * np.sqrt(1 - damping_factor**2)
    print("Damping factor:", damping_factor, alpha/w0)
    print("Frequency of oscillation:", wd, "[rad/s]", "in Hertz:", wd/6.28, "[Hz]")
    print("Poles:")
    print("s1:", s1)
    print("s2:", s2)

#---------------------------------------------------------------------------------------------------
# Parallel RLC circuit:

# Output: inductor current

# Writing a KCL to the node and substituting the characteristic equation of the inductor, we get
# d^2(I_L)/dt^2 + 1/(RC) dI_L/dt + I_L/(LC) = I_source

# and the following characteristic equation of the natural response
# s^2 + 2 alpha s + w0^2 = 0
# s^2 + 1/(2*RC) s + w0^2 = 0

# The solution is of the form (Vp = particular solution)
# I_L(t) = It + Ip

print("---------------------------Parallel RLC circuit----------------------------------------")

R = 50
L = 30 * 10**(-3)
C = 100 * 10**(-6)

print("Natural frequency:", w0, "[rad/s]")
# Damping rate
alpha = 1/(2*R*C)
print("Damping rate:", alpha, "[1/s]")
# Time to zero (4 tau)
print("Time before exponential term goes to zero:", 4 * 1/alpha, "[s]")
# Damping factor
damping_factor = alpha / w0

# The poles are given by
if alpha == w0 : # or if damping_factor = 1
    print("Critically damped system: poles are real and s1 = s2")
    s1 = -alpha
    s2 = -alpha
    print("s1:", s1)
    print("s2:", s2)
elif alpha > w0: # or if damping_factor > 1
    print("Over damped system: poles are real but s1 != s2")
    s1 = - alpha + np.sqrt(alpha**2 - w0**2) 
    s2 = - alpha - np.sqrt(alpha**2 - w0**2)
    print("s1:", s1)
    print("s2:", s2)
else: # or if damping_factor < 1
    print("Under damped system: poles are complex conjugate")
    s1 = -alpha + 1j * np.sqrt(-alpha**2 + w0**2) 
    s2 = -alpha - 1j * np.sqrt(-alpha**2 + w0**2)
    # Csi = damping factor
    damping_factor = 0.5 * (1/R) * np.sqrt(L/C) # or alpha/w0
    # I can write the poles also as s1,2 = -alpha +- 1j*w0*np.sqrt(1-damping_factor**2) = -alpha +- 1j*wd
    wd = w0 * np.sqrt(1 - damping_factor**2)
    print("Damping factor:", damping_factor, alpha/w0)
    print("Frequency of oscillation:", wd, "[rad/s]", "in Hertz:", wd/6.28, "[Hz]")
    print("Poles:")
    print("s1:", s1)
    print("s2:", s2)
