import matplotlib.pyplot as plt
import math
from math import sin, cos, pi, sqrt, log
#Zad1 TABELA NR 5
f_s = 8000

phi = pi/120
funkcja_x = lambda t: sin(2*pi*f_s*t*cos(3*pi*t) + t*phi) 

#sekundy
T = 2

def generate_signal(funkcja, f_s, T):
  return [funkcja(n/f_s) for n in range(int(T*f_s))]
x = generate_signal(funkcja_x, f_s, T)
plt.plot(range(T*f_s), x)

funkcja_y = lambda t: (2*t*sin(0.5*t*pi) + 1.5)*cos(9*pi*t+pi*t)
y = generate_signal(funkcja_y, f_s, T)
plt.plot(range(len(y)), y)

#Zad2 TABELA NR 5
plt.plot(range(1000), x[:1000])

funkcja_z = lambda t: funkcja_x(t)*funkcja_y(t)+ abs(funkcja_x(t)+2)*(funkcja_y(t)**2 + 0.32)
z = generate_signal(funkcja_z, f_s, T)
plt.plot(range(len(z)), z)

#Zad3
funkcja_v = lambda t: sqrt(abs(funkcja_x(t)*funkcja_z(t)+10))*(abs(funkcja_y(t) + 1.2))*sin(2*pi*t)
v = generate_signal(funkcja_v, f_s, T)
plt.plot(range(len(v)), v)

T_u = 3.1

def funkcja_u(t):
  if t<0 or t >= 3.1:
    raise Exception("Wrong time!!")
  if t < 1.2:
    return (-t**2 + 0.5)*sin(30*pi*t)*log(t**2+1,2)
  if t < 2:
    return (1/t)*0.8*sin(24*pi*t)-0.1*t
  if t < 2.4:
    abs(sin(2*pi*t*2))**0.8
  if t < 3.1:
    return 0.23*sin(20*pi*t)*sin(12*pi*t)



u = generate_signal(funkcja_u, f_s, T_u)
plt.plot(range(len(u)), u)

#Zad4 TABELA NR 3
f_s = 22.05
T = 1

from functools import partial

def funkcja_b_k(t, k):
  H = [2,20,40]
  return sum([(cos( 2*pi *h*t + sin(6*pi*t)))*((-1)**h)/(3*h**2) for h in range(1, H[k-1])])



b_1 = generate_signal(partial(funkcja_b_k,k=1), f_s, T_u)
b_2 = generate_signal(partial(funkcja_b_k,k=2), f_s, T_u)
b_3 = generate_signal(partial(funkcja_b_k,k=3), f_s, T_u)

plt.plot(range(len(b_1)), b_1)
plt.plot(range(len(b_2)), b_2)
plt.plot(range(len(b_3)), b_3)

