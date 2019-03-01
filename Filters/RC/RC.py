import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

c = 100 * 10**(-6)
v = 5
r = 2000

t = np.linspace(0,1,1000)

q = c*v*(1-np.exp((-1/(r*c))*t))
i = (v/r)*np.exp((-1/(r*c))*t)

plt.plot([0,t[-1]],[c*v,c*v],label='Charge peak')
plt.plot(t,q,label='Charge of the capacitor (C)')
plt.plot(t,i,label='Current (A)')

print('Tau',1/(r*c))
print('Peak current (A)',v/r)

plt.xlabel('Time (s)')
plt.title('RC circuit')
plt.legend()
plt.show()
