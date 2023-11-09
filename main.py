from math import sin, cos

import time

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def diff(x: float, f: object, dx: float = 1e-6):
    return (f(x + dx) - f(x - dx)) / (2*dx)


def diff2(x: float, f: object, dx: float = 1e-6):
    return (diff(x+dx, f) - diff(x-dx, f)) / (2*dx)


def gradient_descent(x0: float, f: object, learning_rate: float = 0.01, step: int = 10):
    x = [x0]

    for i in range(step):
        new_x = x[-1] - (learning_rate * diff(x[-1], f))
        x.append(new_x)
    
    return x


def newton_method(x0: float, f: object, step: int = 10):
    x = [x0]

    for i in range(step):
        new_x = x[-1] - (diff(x[-1], f) / diff2(x[-1], f))
        x.append(new_x)
    
    return x


def f(x):
    for i in range(10000):
        pass
    return np.sin(x)*5+ np.cos(x/2)*3 + x


fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-15, 15)


x = np.linspace(-10, 10, 2000)
y = f(x)

line, = plt.plot(x, y)
dot, = plt.plot([], [], 'bo')

def update(frame):
    x = frame
    y = f(frame)
    dot.set_data(x, y)
    return dot,


x0 = 0

start_nm100 = time.time()
nm = newton_method(x0, f, step=100)
end_nm100 = time.time()

start_nm4 = time.time()
nm = newton_method(x0, f, step=4)
end_nm4 = time.time()

start_gd100 = time.time()
gd = gradient_descent(x0, f, step=100)
end_gd100 = time.time()

res = []
for i in range(len(nm) - 1):
    delta = nm[i+1] - nm[i]
    for j in range(26):
        res.append(nm[i] + (delta*(j/25)))
nm = res

print("Newton Method 4 times: ", end_nm4 - start_nm4)
print("Newton Method 100 times: ", end_nm100 - start_nm100)
print("Gradient Descent 100 times: ", end_gd100 - start_gd100)
print()

anim_gd = FuncAnimation(fig, update, frames=gd, interval = 50)
anim_nm = FuncAnimation(fig, update, frames=nm, interval = 50)

anim_gd.save('anim_gd.gif', writer='imagemagick')
anim_nm.save('anim_nm.gif', writer='imagemagick')
plt.show()
