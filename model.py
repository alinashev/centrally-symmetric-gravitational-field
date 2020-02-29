import matplotlib.pyplot as plt

def Fx(x_n, y_n):
    return -G * m * M * x_n / (x_n ** 2 + y_n ** 2) ** (3 / 2)

def Fy(x_n, y_n):
    return -G * m * M * y_n / (x_n ** 2 + y_n ** 2) ** (3 / 2)

def step_method(X_n_prev_2, VX_n_prev_1, Y_n_prev_2, VY_n_prev_1):
    X_n = X_n_prev_2 + 2 * dt * VX_n_prev_1
    Y_n = Y_n_prev_2 + 2 * dt * VY_n_prev_1
    VX_next = VX_n_prev_1 + 2 * dt * 1 / m * Fx(X_n, Y_n)
    VY_next = VY_n_prev_1 + 2 * dt * 1 / m * Fy(X_n, Y_n)
    return [X_n, VX_next, Y_n, VY_next]

G = 1
m = 1
M = 100
V_x = [-3.155]
V_y = [0]
X = [0]
Y = [20]
dt = 0.001
t = 0
T = [t]

t = t + dt
VX_n = V_x[0] + dt * Fx(X[0], Y[0])
X_n = X[0] + VX_n * dt
VY_n = V_y[0] + dt * Fy(X[0], Y[0])
Y_n = Y[0] + VY_n * dt

X.append(X_n)
Y.append(Y_n)
V_x.append(VX_n)
V_y.append(VY_n)

i = 2

while t < 200:
    X_n, VX_next, Y_n, VY_next = step_method(X[i - 2], V_x[i - 1], Y[i - 2], V_y[i - 1])
    if ((X_n ** 2 + Y_n ** 2) < 10 ** (-3)):
        break
    X.append(X_n)
    Y.append(Y_n)
    V_x.append(VX_next)
    V_y.append(VY_next)
    T.append(t)
    t = t + dt
    i = i + 1

plt.plot(X,Y)
plt.ylabel('y')
plt.xlabel('x')
plt.grid()
plt.show()


