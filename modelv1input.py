import math
from model_1 import modelv1 as m

# Customise your parameters and their values
c = 1373
p = 2600
lmbda = 1
temp_alpha = 1600
temp_slag = 25
temp_wall = 25
temp_air = 25
heat_lance = 2415600000
mu = 0.026
r = 2
h = 4
d = 0.2
area_wall = 2 * math.pi * r * h
area_air = math.pi * r**2
V = math.pi * (r**2) * h

# Finding values for alpha and beta based off your parameters
#alpha = eval(input('Enter equation for alpha: '))
#beta = eval(input('Enter equation for beta: '))

#alpha = lmbda * area_wall * (temp_alpha - temp_wall) / (heat_lance * d) 
#beta = mu * area_air * (temp_alpha - temp_air) / (heat_lance * d)
#gamma = alpha + beta

gammas = [0.9]
for gamma in gammas:
    m.plot(gamma)
plt.show()

