import numpy as np

def main():
    while True:
        num_of_var = input('Input number of equations: ')
        num_of_var = int(num_of_var)
        if num_of_var < 0:
            continue
        break

    a = []
    b = []
    for i in range(num_of_var):
        while True:
            line = input("Input coefficients (a{0}1 a{0}2 ... b{0}): ".format(i))
            line = line.split(' ')
            if len(line) != num_of_var + 1:
                continue
            a.append([float(x) for x in line[:-1]])
            b.append(float(line[-1]))

            if abs(a[i][i])*2 <= sum([abs(x) for x in a[i]]):
                continue
            break

    a = np.array(a)
    b = np.array(b)

    print("Input A: %s\n" % str(a))
    print("Input b: %s\n" % str(b))

    D = np.diag(np.diag(a))
    LU = (a - D) * -1

    print("D matrix: %s\n" % str(D))
    print("L + U matrix: %s\n" % str(LU))

    Tj = np.dot(np.linalg.inv(D), LU)
    Cj = np.dot(np.linalg.inv(D), b)

    print("Tj matrix: %s\n" % str(Tj))
    print("Cj matrix: %s\n" % str(Cj))

    X = []
    while True:
        line = input("Input x0: ")
        line = line.split(' ')
        if len(line) != num_of_var:
            continue
        X.append([float(x) for x in line])
        break

    while True:
        index = input("Input index of X: ")
        index = int(index)
        if index < 0:
            continue
        break

    for i in range(1, index):
        x_step = np.dot(Tj, X[i-1]) + Cj
        X.append(x_step)

    standard = input("Input standard (1: 0, inf: 1): ")
    standard = int(standard)
    if standard == 0:
        det_T = np.max(np.sum([abs(x) for x in Tj], axis=1))
        print("||T||_1 = %f\n" % det_T)
    elif standard == 1:
        det_T = np.max(np.sum([abs(x) for x in Tj], axis=0))
        print("||T||_inf = %f\n" % det_T)
    else:
        return

    error_type = input("Input error type (pre: 0, post: 1): ")
    error_type = int(error_type)
    error = []
    if error_type == 0:
        if standard == 0:
            for i in range(index):
                e = (det_T**i / (1 - det_T)) * np.sum([abs(x) for x in (X[1] - X[0])])
                error.append(e)
        elif standard == 1:
            for i in range(index):
                e = (det_T**i / (1 - det_T)) * np.max([abs(x) for x in (X[1] - X[0])])
                error.append(e)

    elif error_type == 1:
        if standard == 0:
            for i in range(index):
                if i == 0:
                    error.append(0)
                    continue
                e = (det_T / (1 - det_T)) * np.sum([abs(x) for x in (X[i] - X[i-1])])
                error.append(e)
        elif standard == 1:
            for i in range(index):
                if i == 0:
                    error.append(0)
                    continue
                e = (det_T / (1 - det_T)) * np.max([abs(x) for x in (X[i] - X[i-1])])
                error.append(e)

    for i in range(index):
        print("X%d = %s" % (i, str(X[i])))
        print("Error%d = %.9f\n" % (i, error[i]))


if __name__ == '__main__':
    main()
