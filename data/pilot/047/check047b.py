from sympy import *
a,b,c,d,u=symbols('a b c d u')
rel=a*c-b*d-1
# reduce mod rel: substitute c=(1+bd)/a and clear => check rational identity
def zero_mod(f):
    return simplify(f.subs(c,(1+b*d)/a))==0
x=a*b; y=d*c; z=d*b
print("xy=z(z+1):", zero_mod(x*y-z*(z+1)))
sR=y-x*(x-u**3); f=x-sR**2-u**3; g=z-sR*x
v=a**3*b-a**2*u**3-d**2
hh=x-u**3; C1=c**2-b**2*hh; al=a**2*(1-2*b*d); be=d**2*(3+2*b*d)+al*hh
print("f=C1 v:", zero_mod(f-C1*v), " g=b^2 v:", zero_mod(g-b**2*v), " v=al f+be g:", zero_mod(v-al*f-be*g), " alC1+beb^2=1:", zero_mod(al*C1+be*b**2-1))
# E_+ example
Ep={a:0,d:0,u:0,b:a,c:d}
def Der(f): return expand(sum(diff(f,t)*Ep[t] for t in [a,b,c,d,u]))
print("E+ rel:", Der(rel), " E+ v:", Der(v), " E+^2 v:", Der(Der(v)))
# weights: fiber
wt={a:1,d:1,b:-1,c:-1,u:0}; aux={a:0,d:3,b:-3,c:0,u:2}
def degs(f,W): return set(sum(W[t]*e for t,e in zip([a,b,c,d,u],m)) for m in Poly(expand(f),a,b,c,d,u).monoms())
print("fiber wt v:",degs(v,wt)," aux rel:",degs(rel,aux)," aux N:",degs(d**2+a**2*u**3,aux)," aux a^3b:",degs(a**3*b,aux))
# auxiliary: degree of f,g weights
