from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

# Function to plot our curve
def plot(gamma):
    
    # Defines our ODE (i.e. dT/dt = 1 - gamma * T)
    def dT_dt(T, t):
        return 1 - gamma * T
    
    # Exact solution as solved analytically (can be done by hand)
    def exact(t, gamma):
        return (1 - math.e**(-gamma * t)) / gamma 
    
    # Solves the ODE numerically using the ODEint scipy method
    def numerical_scipy(gamma, T0, time_points):
        solution = odeint(lambda T, t : dT_dt(T, t), T0, time_points)
        return solution[:, 0]
    
    # Solves the ODE numerically using the Euler method of approximation
    def numerical_euler(func, T0, time_points, gamma):
        T = np.zeros_like(time_points)
        T[0] = T0
        
        for i in range(1, len(time_points)):
            dt = time_points[i]- time_points[i - 1]
            T[i] = T[i - 1] + dt * func(T[i - 1], time_points[i - 1])
        return T
    
    # Defines initial condition and the time axis
    T0 = 0.0
    time_points = np.linspace(0, 10, 100)
    
    # Defining our solutions explicitly and plotting
    exact_solution = exact(time_points, gamma)
    temp_solution = numerical_scipy(gamma, T0, time_points)
    numerical_soln = numerical_euler(dT_dt, T0, time_points, gamma)
    
    plt.plot(time_points, temp_solution, label = f'ODEint, \u03B3 = {gamma}')
    plt.plot(time_points, numerical_soln, label = f'Euler, \u03B3 = {gamma}')
    plt.plot(time_points, exact_solution, label = f'Exact, \u03B3 = {gamma}')
    plt.xlabel("t'")
    plt.ylabel("T'")
    plt.legend()