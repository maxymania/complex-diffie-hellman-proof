#
def i2p(x):
    return (x&(1<<y) for y in range(x.bit_length()))
#
def mult5(a,b):
    ar,ai=a
    br,bi=b
    cr = sub4(mult4(ar,br),mult4(ai,bi))
    ci = add4(mult4(ai,br),mult4(ar,bi))
    return cr,ci
#
def add4(a,b):
    ar,ai=a
    br,bi=b
    cr = add3(ar,br)
    ci = add3(ai,bi)
    return cr,ci
def sub4(a,b):
    ar,ai=a
    br,bi=b
    cr = sub3(ar,br)
    ci = sub3(ai,bi)
    return cr,ci
def mult4(a,b):
    ar,ai=a
    br,bi=b
    cr = sub3(mult3(ar,br),mult3(ai,bi))
    ci = add3(mult3(ai,br),mult3(ar,bi))
    return cr,ci
#
def add3(a,b):
    ar,ai=a
    br,bi=b
    cr = add2(ar,br)
    ci = add2(ai,bi)
    return cr,ci
def sub3(a,b):
    ar,ai=a
    br,bi=b
    cr = sub2(ar,br)
    ci = sub2(ai,bi)
    return cr,ci
def mult3(a,b):
    ar,ai=a
    br,bi=b
    cr = sub2(mult2(ar,br),mult2(ai,bi))
    ci = add2(mult2(ai,br),mult2(ar,bi))
    return cr,ci
#
def add2(a,b):
    ar,ai=a
    br,bi=b
    cr = add(ar,br)
    ci = add(ai,bi)
    return cr,ci
def sub2(a,b):
    ar,ai=a
    br,bi=b
    cr = sub(ar,br)
    ci = sub(ai,bi)
    return cr,ci
def mult2(a,b):
    ar,ai=a
    br,bi=b
    cr = sub(mult(ar,br),mult(ai,bi))
    ci = add(mult(ai,br),mult(ar,bi))
    return cr,ci
#
def add(a,b):
    ar,ai=a
    br,bi=b
    cr = (ar+br)
    ci = (ai+bi)
    return (cr&255),(ci&255)
def sub(a,b):
    ar,ai=a
    br,bi=b
    cr = (ar-br)
    ci = (ai-bi)
    return (cr&255),(ci&255)
def mult(a,b):
    ar,ai=a
    br,bi=b
    cr = ((ar*br)&255)-((ai*bi)&255)
    ci = ((ai*br)&255)+((ar*bi)&255)
    return (cr&255),(ci&255)
#
def pow(num,power):
    r=(((((1,0),(0,0)),((0,0),(0,0))),(((0,0),(0,0)),((0,0),(0,0)))),
       ((((0,0),(0,0)),((0,0),(0,0))),(((0,0),(0,0)),((0,0),(0,0)))))
    for ok in power:
        if ok:
            r=mult5(r,num)
    return r
#
g=(((((1,2),(3,5)),((3,1),(6,2))),(((4,7),(1,7)),((2,3),(3,6)))),
   ((((9,5),(7,3)),((2,5),(5,3))),(((6,5),(1,6)),((2,4),(1,2)))))
#p=65536
#p=65537

a=list(i2p(100))
b=list(i2p(77))
A = pow(g,a)
B = pow(g,b)
Ka = pow(B,a)
Kb = pow(A,b)

print()
#print(g)
#print(A)
#print(B)
print(Ka)
print()
print(Kb)
#
