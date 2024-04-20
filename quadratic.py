import math


def roots(a,b,c):
    D=b**2-4*a*c
    x1= (-b+(D)**0.5)/2
    x2= (-b-(D)**0.5)/2
    if x1==x2:
        return f'({x1})'
    else:
        if D>=0:
            return f'({x1}, {x2})'
        else:
            return f'( )'


def value_y(a, b, c, x):
        y= a*x**2+b*x+c
        return y


def to_string(a, b, c):
    y= f" {a} * X^2 + {b} * X + {c}"
    y2= f" {a} * X^2"
    y3= f" {a} * X^2 + {b} * X"
    y4= f" {a} * X^2 + {c}"
    y5= f" {b} * X"
    y6= f" {b} * X + {c}"
    y7= f" {c}"
    if a!=0 and b!=0 and c!=0:
        return f"f(x) ={y}"
    elif a!=0 and b==0 and c==0:
        return f"f(x) ={y2}"
    elif a!=0 and b!=0 and c==0:
        return f"f(x) ={y3}"
    elif a!=0 and b==0 and c!=0:
        return f"f(x) ={y4}"
    elif a==0 and b!=0 and c==0:
        return f"f(x) ={y5}"
    elif a==0 and b!=0 and c!=0:
        return f"f(x) ={y6}"
    else:
        return f"f(x) ={y7}"



def derivation(a, b, c):
    d= f"{2*a} * X + {b}"
    d2= f"{b}"
    d3= f"{2*a} * X"
    d4= 0
    if a!=0 and b!=0:
        return f"f'(x) = {d}"
    elif a==0 and b!=0:
        return f"f'(x) = {d2}"
    elif a!=0 and b==0:
        return f"f'(x) = {d3}"
    else:
        return f"f'(x) = {d4}"

