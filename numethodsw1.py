from math import *

def bisectionmethod(f, a, b, tol,n):
    i=1
    while i<=n:
        p=a+(b-a)/2
        print("Iteration",i,"p=",p)
        if abs(f(p)) <= 1e-15 or (b-a)/2 < tol:
            return p
        i+=1
        if f(p)*f(a) > 0:
            a=p
        else:
            b=p
    print("Method failed after",n,"iterations.")
    return None

def newtonmethod(f, df, p0, tol, n):
    i=1
    while i<=n:
        p=p0-f(p0)/df(p0)
        print("Iteration",i,"p=",p)
        if abs(p-p0) < tol:
            return p
        p0=p
        i+=1
    print("Method failed after",n,"iterations.")
    return None  

def secantmethod(f, t0, t1, tol,n):
    i=2
    while i<=n:
        t=t1-f(t1)*(t1-t0)/(f(t1)-f(t0))
        print("Iteration",i,"t=",t)
        if abs(t-t1) < tol:
            return t
        t0=t1
        t1=t
        i+=1
    print('Error, out of iterarions')
    return

def fixedpointmethod(f, p0, tol, n):
    i=1
    while i<=n:
        p=f(p0)
        print("Iter= ",i,"; p=",  p)
        if abs(p-p0)< tol:
            return p
        p0=p
        i=+1
    print("Error: run out of iterarions")
    return None
    




