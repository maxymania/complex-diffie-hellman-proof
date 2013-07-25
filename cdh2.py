#
def i2p(x):
    return (x&(1<<y) for y in range(x.bit_length()))
#
def mult2(a,b,m):
    ar,ai=a
    br,bi=b
    cr = sub(mult(ar,br,m),mult(ai,bi,m),m)
    ci = add(mult(ai,br,m),mult(ar,bi,m),m)
    return cr,ci
#
def add(a,b,m):
    ar,ai=a
    br,bi=b
    cr = (ar+br)
    ci = (ai+bi)
    return (cr%m),(ci%m)
def sub(a,b,m):
    ar,ai=a
    br,bi=b
    cr = (ar-br)
    ci = (ai-bi)
    return (cr%m),(ci%m)
def mult(a,b,m):
    ar,ai=a
    br,bi=b
    cr = (ar*br)-(ai*bi)
    ci = (ai*br)+(ar*bi)
    return (cr%m),(ci%m)
#
def pow(num,power,m):
    r=((1,0),(0,0))
    for ok in power:
        if ok:
            r=mult2(r,num,m)
    return r
#

g=((1,2),(3,5))
#p=65536
p=65537

a=list(i2p(100))
b=list(i2p(77))
A = pow(g,a,p)
B = pow(g,b,p)
Ka = pow(B,a,p)
Kb = pow(A,b,p)

print()
print(g)
print(A)
print(B)
print(Ka)
print(Kb)
#
