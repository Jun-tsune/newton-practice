import newton

def est_func(x):# assuming func y=x^2+2x+1
    y = x**2+2*x+1
    return y

result = newton.optimize(est_func, 4)   ## Assuming your function is called `optimize`.

print(result)
