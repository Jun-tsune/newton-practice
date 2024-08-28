import numpy as np

def derivative(est_func, x, dev_eps, sign):
    """Caluculating first derivative.

    Keyword arguments:
    est_func -- function of research (def)
    x -- point of derivative (int, float)
    dev_eps -- epsilon for derivative (float)
    sin -- derivative orientation (1 or -1)

    Return:
    dev -- an derivative number (int, float)
    """
    dev = x.copy()
    for i in range(len(x)):
        x_2 = x.copy()
        x_2[i] = x[i] + dev_eps * sign
        y = est_func(x)
        y_2 = est_func(x_2)
        dev[i] = (y_2 - y)/(dev_eps * sign)
    return dev 


def sec_derivative(est_func, x, dev_eps, sign):
    """Caluculating second derivative.

    Keyword arguments:
    est_func -- function of research (def)
    x -- point of derivative (int, float)
    dev_eps -- epsilon for derivative (float)
    sin -- derivative orientation (1 or -1)

    Return:
    dev -- an derivative number (int, float)
    """
    dev = np.asarray([x,x,x])
    for i in range(len(x)):
        x_2 = x.copy()
        x_2[i] = x[i] + dev_eps * sign
        y = derivative(est_func, x, dev_eps, sign)
        y_2 = derivative(est_func, x_2, dev_eps, sign)
        dev[i] = (y_2 - y)/dev_eps * sign
    return dev


def optimize(est_func, x, dev_eps = 10**(-6), threshold = 10**(-4), max_iter=10000):
    """Caluculating optimized points.

    Keyword arguments:
    est_func -- function of research (def)
    x -- starting point of optimization (int, float)
    dev_eps -- epsilon for derivative (float)
    threshold -- threshold of OK (int, float)
    max_iter -- how many times to try optimazation (int, default 10000)

    Return:
    x -- an optimized number (int, float)
    """
    for i in range(max_iter):
        sign = (-1)**i
        dev = derivative(est_func, x, dev_eps, sign)
        sec_dev = sec_derivative(est_func, x, dev_eps, sign)
        dif = np.dot(np.linalg.inv(sec_dev), dev.T)
        x = x - dif
        if np.linalg.norm(dif) < threshold:
            break
    if i == max_iter-1:
        print("max_itter may be small")    
    return x
