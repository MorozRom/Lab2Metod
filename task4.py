import matplotlib.pyplot as plt
def build_points(x_min, x_max, step):
    xs = []
    ys = []
    x = x_min
    while x <= x_max:
        xs.append(x)
        ys.append(x ** 2)
        x = round(x + step, 10)
    return xs, ys
