def derivative(x, est_precision, sign):
    """Caluculating first derivative.

    Keyword arguments:
    x -- point of derivative (int, float)
    est_precision -- search area (int, float)
    sin -- derivative orientation (1 or -1)

    Return:
    dev -- an derivative number (int, float)
    """
    x_2 = x + est_precision * sign
    y = est_func(x)
    y_2 = est_func(x_2)
    dev = (y_2 - y)/est_precision * sign
    return dev 


def sec_derivative(x, est_precision, sign):
    """Caluculating second derivative.

    Keyword arguments:
    x -- point of derivative (int, float)
    est_precision -- search area (int, float)
    sin -- derivative orientation (1 or -1)

    Return:
    dev -- an derivative number (int, float)
    """
    x_2 = x + est_precision * sign
    y = derivative(x, est_precision, sign)
    y_2 = derivative(x_2, est_precision, sign)
    dev = (y_2 - y)/est_precision * sign
    return dev


def optimize(x, itter=10000):
    """Caluculating optimized points.

    Keyword arguments:
    x -- starting point of optimization (int, float)
    itter -- how many times to try optimazation (int, default 10000)

    Return:
    x -- an optimized number (int, float)
    """
    for i in range(itter):
        est_precision = 1/((i+1)*100)
        sign = (-1)**i
        dev = derivative(x, est_precision, sign)
        sec_dev = sec_derivative(x, est_precision, sign)
        x = x - dev/sec_dev
    return x