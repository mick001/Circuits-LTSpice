import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

l = 0.0229      #Inductance (H)
r = 3.34        #Resistance (Ohm)
v = 5           #Voltage (V) DC
i = v/r         #Peak current (A)
tau = l/r       #Tau time constant
a = tau * 4.4   #critical time value at which current is switched (switching occurs every a seconds)

t = np.linspace(0,2*a,2000) #Time vector

#-------------------------------------------------------------------------------
#1st on-cycle current

def initialCurrent():
    current = []
    for i in t:
        if i <= a:
            current.append((v/r)*(1-np.exp((-r/l)*i)))          #I(t) = v/r*[1-exp((-r/l)*t)]
        else:
            current.append(0)
    return np.array(current)

#Plot Icurrent
Icurrent = initialCurrent()
plt.plot(t,Icurrent,label='current',color='blue')

#------------------------------------------------------------------------------
#1st off-cycle current

def laterCurrent():
    current = []
    for i in t:
        if i >= a:
            current.append(Icurrent[-1001]*np.exp((-r/l)*(i-a)))  #I(t) = Ir * exp((-r/l)*(t-t0))
        else:
            current.append(0)
    return np.array(current)

#Plot current after switch off
current_off = laterCurrent()
plt.plot(t,current_off,color='blue')


#-------------------------------------------------------------------------------
#Current on and off cycle: on and off at the zeros of the it function
f = 1/(2*a)                 #frequency f = 1/T
w = np.pi/a                 #w = 2pi * f
it = i*np.sin(w*t)
plt.plot(t,it,label='On/off cycle',color='green')

#Plot zeros (switching points)
zeros = np.array([0,a,2*a])
zeros_i = i*np.sin(w*zeros)
plt.plot(zeros,zeros_i,marker='x',markersize=10,label='On and off',color='red')
plt.annotate('On',xy=(zeros[0]+0.0005,zeros_i[0]))
plt.annotate('Off',xy=(zeros[1]+0.0005,zeros_i[1]))
plt.annotate('On',xy=(zeros[2]+0.0005,zeros_i[2]))

#Critical value plot
plt.plot((a,a+0.00001),(max(it),min(it)),'r',alpha=0.9,label='Critical value')

#-------------------------------------------------------------------------------
#Print some data
print('Inductance (H):','\t'+str(l))
print('Resistance (Ohm):','\t'+str(r))
print('DC voltage (V):','\t'+str(v))
print('Current (A):','\t\t'+str(i))
print('Tau:','\t\t\t'+str(tau))
print('Critical time (s):','\t'+str(a))
print('\n')
print('Switch frequency (Hz):','\t'+str(f))
print('w coefficient (2*pi*f)','\t'+str(w))

#-------------------------------------------------------------------------------
#Plot settings

#x axis line
plt.plot((0,2*a+0.0005),(0,0),'k',alpha=0.9,markersize=10)

#Axis labels
plt.xlabel('time (s)')
plt.ylabel('current (A)')

#Legend and limits
plt.legend(loc=3,fancybox=True,shadow=True)
plt.xlim(-0.002,2*a+0.003)
plt.ylim(min(it)-0.05,max(it)+0.05)

plt.show()

#-------------------------------------------------------------------------------
