#
def i2p(x):
    return (x&(1<<y) for y in range(x.bit_length()))
#
def mult4(a,b,m):
    ar,ai=a
    br,bi=b
    cr = sub3(mult3(ar,br,m),mult3(ai,bi,m),m)
    ci = add3(mult3(ai,br,m),mult3(ar,bi,m),m)
    return cr,ci
#
def add3(a,b,m):
    ar,ai=a
    br,bi=b
    cr = add2(ar,br,m)
    ci = add2(ai,bi,m)
    return cr,ci
def sub3(a,b,m):
    ar,ai=a
    br,bi=b
    cr = sub2(ar,br,m)
    ci = sub2(ai,bi,m)
    return cr,ci
def mult3(a,b,m):
    ar,ai=a
    br,bi=b
    cr = sub2(mult2(ar,br,m),mult2(ai,bi,m),m)
    ci = add2(mult2(ai,br,m),mult2(ar,bi,m),m)
    return cr,ci
#
def add2(a,b,m):
    ar,ai=a
    br,bi=b
    cr = add(ar,br,m)
    ci = add(ai,bi,m)
    return cr,ci
def sub2(a,b,m):
    ar,ai=a
    br,bi=b
    cr = sub(ar,br,m)
    ci = sub(ai,bi,m)
    return cr,ci
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
    cr = ((ar*br)%m)-((ai*bi)%m)
    ci = ((ai*br)%m)+((ar*bi)%m)
    return (cr%m),(ci%m)
#
def pow(num,power,m):
    r=((((1,0),(0,0)),((0,0),(0,0))),(((0,0),(0,0)),((0,0),(0,0))))
    for ok in power:
        if ok:
            r=mult4(r,num,m)
    return r
#
g=((((1,2),(3,5)),((3,1),(6,2))),(((4,7),(1,7)),((2,3),(3,6))))
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
