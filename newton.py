def est_func(x):# assuming func y=x^2+2x+1
    y = x**2+2*x+1
    return y
def derivative(x, est_precision, sign):
    x_2 = x + est_precision * sign
    y = est_func(x)
    y_2 = est_func(x_2)
    return (y_2 - y)/est_precision * sign
def sec_derivative(x, est_precision, sign):
    x_2 = x + est_precision * sign
    y = derivative(x, est_precision, sign)
    y_2 = derivative(x_2, est_precision, sign)
    return (y_2 - y)/est_precision * sign
def optimize(x, itter=10000):
    for i in range(itter):
        est_precision = 1/((i+1)*100)
        sign = (-1)**i
        dev = derivative(x, est_precision, sign)
        sec_dev = sec_derivative(x, est_precision, sign)
        x = x - dev/sec_dev
    return x

newton.optimize(5, 100000)