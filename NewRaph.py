# newton_raphson.py

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        if df(x) == 0:
            print("Derivative is zero. Cannot proceed.")
            return None
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    print("Did not converge.")
    return None

# test.py

from newton_raphson import newton_raphson

def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

root = newton_raphson(f, df, 1.5)
print("Root is:", root)
