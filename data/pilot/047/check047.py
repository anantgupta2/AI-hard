from sympy import *
p,s,u,F,J,w,Lv,Mv,Z=symbols('p s u F J w L M Z')
x=s**2+u**3+p**2*F
y=s+x*(x-u**3)
z=s*x+p**2*J
H=x**2*F-(1+2*s*x)*J-p**2*J**2-p*u
print("identity xy-z(z+1)=p^2(H+pu):", expand(x*y-z*(z+1)-p**2*(H+p*u))==0)
# Delta derivation on P: values
D={p:0,u:-p**2,s:-3*p**2*x*u**2,F:(6*s*x+3)*u**2,J:3*x**2*u**2,w:0}
def Der(f):
    return expand(sum(diff(f,v)*D[v] for v in [p,s,u,F,J,w]))
# check Delta fixes x,y,z
print("Delta x,y,z:", [Der(t) for t in [x,y,z]])
print("Delta H:", factor(Der(H)), " Delta^2 H:", Der(Der(H)))
# Lin coords
x0=s**2+u**3
L_=x0**2*F-(1+2*s*x0)*J; M_=(1-2*s*x0)*F+4*s**2*J
Fi=4*s**2*Lv+(1+2*s*x0)*Mv; Ji=-(1-2*s*x0)*Lv+x0**2*Mv
print("inverse:", expand(L_.subs({F:Fi,J:Ji},simultaneous=True)-Lv), expand(M_.subs({F:Fi,J:Ji},simultaneous=True)-Mv))
HL=expand(H.subs({F:Fi,J:Ji},simultaneous=True))
FL=Fi; JL=Ji
Q=2*x0*FL**2-2*s*FL*JL-JL**2
print("H expansion:", expand(HL-(Lv-p*u+p**2*Q+p**4*FL**3))==0)
C=expand(Q.subs(Lv,0))
print("C formula:", expand(C-Mv**2*(2*x0+6*s*x0**2+4*s**2*x0**3-x0**4))==0)
Q1=cancel((Q-C)/Lv); Q1=expand(Q1)
Ls=p*u-p**2*C
print("root:", expand(HL.subs(Lv,Ls)-p**3*((u-p*C)*Q1.subs(Lv,Ls)+p*FL.subs(Lv,Ls)**3))==0)
h=u-p*Q-p**3*FL**3-p**2*w
e0=-w-p*FL**3-Q1*h
print("H+p^3w = L - p h:", expand(HL+p**3*w-(Lv-p*h))==0)
print("e certificate:", expand(p**3*e0-(Lv-Ls)-(p**2*Q1-1)*(HL+p**3*w))==0)
Wz=expand(HL.subs(Lv,Ls+p**3*Z))
print("H(L*+p^3Z) divisible by p^3:", all(rem(c,p**3,p)==0 for c in Poly(Wz,Z).all_coeffs()) if True else None)
print("Htop identity:", expand(x*y-z*(z+1)-p**2*(H+p*u)) )
