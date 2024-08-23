def derivative(est_func, x, est_precision, sign):
    """Caluculating first derivative.

    Keyword arguments:
    est_func -- function of research (def)
    x -- point of derivative (int, float)
    est_precision -- search area (int, float)
    sign -- derivative orientation (1 or -1)

    Return:
    dev -- an derivative number (int, float)
    """
    x_2 = x + est_precision * sign
    y = est_func(x)
    y_2 = est_func(x_2)
    dev = (y_2 - y)/est_precision * sign
    return dev 


def sec_derivative(est_func, x, est_precision, sign):
    """Caluculating second derivative.

    Keyword arguments:
    est_func -- function of research (def)
    x -- point of derivative (int, float)
    est_precision -- search area (int, float)
    sign -- derivative orientation (1 or -1)

    Return:
    dev -- an derivative number (int, float)
    """
    x_2 = x + est_precision * sign
    y = derivative(est_func, x, est_precision, sign)
    y_2 = derivative(est_func, x_2, est_precision, sign)
    dev = (y_2 - y)/est_precision * sign
    return dev


def optimize(est_func, x, threshold = 10**(-6), max_iter=10000):
    """Caluculating optimized points.

    Keyword arguments:
    est_func -- function of research (def)
    x -- starting point of optimization (int, float)
    threshold -- threshold of OK (int, float)
    max_iter -- how many times to try optimazation (int, default 10000)

    Return:
    x -- an optimized number (int, float)
    """
    for i in range(max_iter):
        est_precision = 1e-6
        sign = (-1)**i
        dev = derivative(est_func, x, est_precision, sign)
        sec_dev = sec_derivative(est_func, x, est_precision, sign)
        x = x - dev/sec_dev
        if abs(dev/sec_dev) < threshold:
            break
    if i == max_iter-1:
        print("max_itter may be small")    
    return x