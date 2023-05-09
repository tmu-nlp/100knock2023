def gen_str(x, y, z):
    return "{}時の{}は{}".format(x, y, z)


x_t = 12
y_t = "気温"
z_t = 22.4

print(gen_str(x_t, y_t, z_t))
