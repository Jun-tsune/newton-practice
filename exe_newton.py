import newton
import numpy as np

x = np.asarray([1,2,3]) #starting point

def est_func(x):# assuming func y=x^2+y^3+z^2+xyz
    y = x[0]**2+x[1]**3+x[2]**2+x[0]*x[1]*x[2]
    return y

result = newton.optimize(est_func, x)   ## Assuming your function is called `optimize`.

print(result)
