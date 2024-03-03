from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def main():
    def solve_ode(gamma, T0, time_points):
        def temp_derivative(T, t):
            return 1 - gamma * T
        solution = odeint(temp_derivative, T0, time_points)
        return solution[:, 0]
    
    T0 = 0.0
    time_points = np.linspace(0, 10, 100)
    gamma = float(input('Enter a value for gamma: '))
    
    temp_solution = solve_ode(gamma, T0, time_points)
    plt.plot(time_points, temp_solution, label = f'Gamma = {gamma}')
    plt.xlabel('Scaled Time')
    plt.ylabel('Scaled Temperature')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
