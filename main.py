# ===== 2 lab =====

def bisection(f, a, b, eps, max_iter):
    print()
    print('BISECTION[', a, b, '] >> Started')
    if f(a) * f(b) >= 0:
        print('BISECTION >> Failed (not started):[', a, ';', b, ']')
        return None
    a_n = a
    b_n = b
    for n in range(1, max_iter + 1):
        if abs(a_n - b_n) < eps:
            print('BISECTION >> Succeeded for [', a, ';', b, '] :', n,
                  'iterations')
            return '%.6f' % a_n, '%.6f' % b_n
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0:
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
        elif f_m_n == 0:
            return '%.6f' % m_n
        else:
            print('BISECTION >> Failed for [', a_n, ';', b_n, ']:', n,
                  'iteration')
            return None
    print('BISECTION >> Failed for [', a_n, ';', b_n, ']: Exceeded',
          max_iter, 'iterations')
    return None


def fixed_point(f, df, a, b, eps, max_iter):
    print()
    print('FIXEDPOINT[', a, b, '] >> Started')
    m = df(a)
    M = df(b)
    #print('m, M:', m, M)
    if 0 > m * M:
        print('FIXEDPOINT >> Failed: m * M < 0')
        return None

   # if 0 < min(m, M):
    tau = -2 / (m + M)

    xn = (a + b) / 2
    xm = xn + eps
    for n in range(1, max_iter + 1):
        fxn = f(xn)
        xm = xn
        xn = xn + fxn * tau
        #print('xn - xm:', xn - xm)
        if abs(xm - xn) < eps and abs(fxn) < eps:
            print('FIXEDPOINT >> Succeeded for [', a, ';', b, '] :', n,
                  'iterations')
            return '%.6f' % xn
    print('FIXEDPOINT >> Failed: Exceeded', max_iter, 'iterations')
    return None


def func(x):
    return x**5 - 2*x - 0.2


def dfunc(x):
    return 5*x**4 - 2


eps = 1e-5
upper = 30

print('f(x) = x**5 - 2*x - 0.2')
print('EPS:', eps)
print('Loop upper bound:', upper)
print()

print(bisection(func, -2, -1, eps, upper))
print(bisection(func, -1, 0, eps, upper))
print(bisection(func, 0, 2, eps, upper))
print()

print(fixed_point(func, dfunc, -1.2, -1.1, eps, upper))
print(fixed_point(func, dfunc, -0.2, 0, eps, upper))
print(fixed_point(func, dfunc, 1.1, 1.3, eps, upper))
