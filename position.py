import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from vpython import sphere, vector, rate, canvas

df = pd.read_csv('accelerometer_data.csv')

t = df['Time (s)'].values
ax = df['Linear Acceleration x (m/s^2)'].values
ay = df['Linear Acceleration y (m/s^2)'].values
az = df['Linear Acceleration z (m/s^2)'].values

dt = t[1] - t[0]

vx = [0]
vy = [0]
vz = [0]

for i in np.arange(212, len(t) - 1):
    vx.append(vx[-1] + ax[i] * dt)
    vy.append(vy[-1] + ay[i] * dt)
    vz.append(vz[-1] + az[i] * dt)

x = [0]
y = [0]
z = [0]

for i in np.arange(0, 5340):
    x.append(x[-1] + vx[i] * dt)
    y.append(y[-1] + vy[i] * dt)
    z.append(z[-1] + vz[i] * dt)

scene = canvas(title = 'visualisation', width = 800, height = 600)
phone = sphere(pos = vector(x[0], y[0], z[0]), radius = 0.1, make_trail = True)

for i in range(1, len(x)):
    rate(500)
    phone.pos = vector(x[i], y[i], z[i])
    
plt.plot(t[211:], x, label = 'x')
plt.plot(t[211:], y, label = 'y')
plt.plot(t[211:], z, label = 'z')
plt.legend()
plt.grid()
plt.show()