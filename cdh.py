#
def i2p(x):
    return (x&(1<<y) for y in range(x.bit_length()))
#
def mult(a,b,m):
    ar,ai=a
    br,bi=b
    cr = (ar*br)-(ai*bi)
    ci = (ai*br)+(ar*bi)
    return (cr%m),(ci%m)
#
def pow(num,power,m):
    r=(1,0)
    for ok in power:
        if ok:
            r=mult(r,num,m)
    return r
#

#g=(3,5)
g=(1,2)
p=65536
#p=65537

a=list(i2p(100))
b=list(i2p(77))
A = pow(g,a,p)
B = pow(g,b,p)
Ka = pow(B,a,p)
Kb = pow(A,b,p)

print()
print(A)
print(B)
print(Ka)
print(Kb)
#
