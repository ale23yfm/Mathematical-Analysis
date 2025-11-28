#(a),(b),(c) - convex function -> fc
def fc(x):
    return x**2 + 4*x + 5
def fc_prime(x):
    return 2*x + 4
def gradient_desc_c(x0, eta, steps= 15):
    xs = [x0]
    x = x0
    for _ in range(steps):
        x = x - eta*fc_prime(x)
        xs.append(x)
    return xs

#(d) - non-convex function -> fnc
def fnc(x):
    return 2*x**4 - 3*x**2 + 3*x + 5
def fnc_prime(x):
    return 8*x**3 - 6*x + 3
def gradient_desc_nc(x0, eta, steps= 15):
    xs = [x0]
    x = x0
    for _ in range(steps):
        x = x - eta*fnc_prime(x)
        xs.append(x)
    return xs

if __name__ == "__main__":
    fc_min = (-4)/(2*1)
    print (fc_min)
    x0 = 5
    v = gradient_desc_c(x0, 0.1)
    print("\na. ")
    for vv in v:
        print(vv)
    v = gradient_desc_c(x0, 0.2, 5)
    print("\nb. ")
    for vv in v:
        print(vv)
    v = gradient_desc_c(x0, 0.7, 7)
    print("\nc. ")
    for vv in v:
        print(vv)

    start1 = -1.5
    start2 = 1.
    path1 = gradient_desc_nc(start1, 0.01, 2000)
    path2 = gradient_desc_nc(start2, 0.01, 2000)
    x1_final = path1[-1]
    x2_final = path2[-1]
    print("\nd. ")
    print("Start", start1, "-> x_final =", x1_final, " f(x) =", fnc(x1_final))
    print("Start", start2, "-> x_final =", x2_final, " f(x) =", fnc(x2_final))