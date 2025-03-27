# Description: This file contains the implementation of the bisection method and newton method for finding the root of a function.
from numethodsw1 import *
from interpolatingPolynomials import *
def bisection_method():
    print("Bisection method selected.")
    f=lambda x: 10*x**4-3*x*exp(x)-3*exp(x)
    a = 2
    b = 3
    tol = 1e-5
    n = 100
    print("Root of the function is:", bisectionmethod(f, a, b, tol, n))
    
    

def newton_method():
    print("Newton method selected.")
    f=lambda x: 2*sin(x)-x
    df=lambda x: 2*cos(x)-1
    p0=1
    tol=1e-10
    n=100
    print("Root of the function is:", newtonmethod(f, df, p0, tol, n))

def newton_method_quiz():
    print("Newton method selected.")
    f=lambda x: (4*x**2) - (exp(x)) -exp(-x)
    df=lambda x: 8*x - exp(x) + exp(-x)
    p0=-3.0
    tol=1e-4
    n=100
    print("Root of the function 4 quiz is:", newtonmethod(f, df, p0, tol, n))
def newton_method_quiz2():
    print("Newton method selected.")
    f=lambda x: (-x**4)+(6*x**2)+11
    df=lambda x: -4*x**3 + 12*x
    p0=1
    tol=1e-8
    n=100
    print("Root of the function 4 quiz is:", newtonmethod(f, df, p0, tol, n))
def secant_method():
    print("secant method selected")
    vel_function= lambda x: 2200*log((1.6e5)/(1.6e5-2680*x))-9.8*x-1000
    t0=20
    t1=30
    tol= 1e-3
    n=20
    print('Secant nethod for rocket ', secantmethod(vel_function,t0,t1,tol, n))
def secant_method_quiz():
    print("secant method selected")
    vel_function= lambda x: x**5- 3*x**4 + 10*x - 8
    t0=3.0
    t1=3.01
    tol= 1e-3
    n=20
    print('Secant nethod for quiz ', secantmethod(vel_function,t0,t1,tol, n))
def fixedpoint_method():
    print("Fixed point method selected.")
    f=lambda x: pow(2.0, -x)
    p0=0.5
    tol=1e-8
    n=100
    print("Root of the function is:", fixedpointmethod(f, p0, tol, n))

def fixedpoint_method_quiz():
    print("Fixed point method selected.")
    f=lambda x: ((x**2)*sqrt(x**2+1 )) -1
    p0=1.4
    tol=1e-2
    n=100
    print("Root of the function is:", fixedpointmethod(f, p0, tol, n))
def fixedpoint_method_quiz2():
    print("Fixed point method selected.")
    f=lambda x: log(x+1) + 5
    p0=3
    tol=1e-8
    n=100
    print("Root of the function is:", fixedpointmethod(f, p0, tol, n))
def interpolating_newton():
    datos=[(3.0, 2310),(5.0, 3090),(7.0, 3940),(20.0, 8000)]
    # datos= [(-1.0,2.0),(0.0,-1.0),(1.0,1.0),(2.0,-2.0)]
    T, P= newtonPol(datos)
    print("Newton Polynomial")
    print("Table of divided differences")
    pprint(T)
    print("Interpolating Polynomial terms")
    # get T Evaluated in [i][i]
    terms = [T[i][i] for i in range(len(T))]
    print(terms)
    print("evaluating the polynomial in x=4")
    print(P(4))

def interpolating_lagrange():
    datosf= [(0.0, -3.0), (1.0, 0.0),(3.0, 5.0), (6.0,7.0)]
    Pf = lagrangePol(datosf)
    print("Lagrange Polynomial")
    print ("evaluating lagrange Polynomial  in x=1.8")
    print(Pf(1.8))

def main():
    while True:
        print("Select a numerical method:")
        print("1. Bisection Method")
        print("2. Newton Method")
        print("3. Secant Method")
        print("4. Fixed Point Method")
        print("5. Interpolating Newton Polynomial")
        print("6. Interpolating Lagrange Polynomial")
        print("0:exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            bisection_method()
        elif choice == '2':
            newton_method()
        elif choice == '3':
            secant_method()
        elif choice == '4':
            fixedpoint_method()
        elif choice == '5':
            interpolating_newton()
        elif choice == '6':
            interpolating_lagrange()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()