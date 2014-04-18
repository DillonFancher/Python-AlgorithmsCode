from __future__ import division
from numpy import *
from math import *

#H = A + iB
#z = x + iy

A = array([(3, 2),(2, 3)])
B = array([(4, 1),(3, 4)])

x = array([(1), (5)]).reshape(2, 1)
y = array([(-4), (-1)]).reshape(2, 1)


N = len(A)
L = identity(N)
P = identity(N)
U = array([(3, 2),(2, 3)])
Q = array([(4, 1),(3, 4)])

Apiv = arange(N)
Bpiv = arange(N)

for k in range(0, N):
    Acurr_piv = fabs(U[k,k])
    Bcurr_piv = fabs(Q[k,k])
    Anew_piv = k
    Bnew_piv = k
    for p in range(k+1, N):
        if(Acurr_piv < fabs(U[Apiv[p],k])):
            Acurr_piv = fabs(U[Apiv[p],k])
            Anew_piv = p
        if(Bcurr_piv < fabs(U[Bpiv[p],k])):
            Bcurr_piv = fabs(Q[Bpiv[p],k])
            Bnew_piv = p
    
    if(Anew_piv != k):
        AtempPiv = Apiv[k]
        Apiv[k] = Apiv[Anew_piv]
        Apiv[Anew_piv] = AtempPiv    
        for i in range(0, k-1):
            AtempL = L[k, i]
            L[k, i] = L[Anew_piv, i]
            L[Anew_piv, i] = AtempL
    
    if(Bnew_piv != k):
        BtempPiv = Bpiv[k]
        Bpiv[k] = Bpiv[Anew_piv]
        Bpiv[Bnew_piv] = BtempPiv    
        for i in range(0, k-1):
            BtempL = P[k, i]
            P[k, i] = P[Bnew_piv, i]
            P[Bnew_piv, i] = BtempL
    
    for i in range(k+1, N):
        L[i,k] = U[Apiv[i], k]/U[Apiv[k],k]
        P[i,k] = Q[Bpiv[i], k]/Q[Bpiv[k],k]
        for j in range(0, N):
            U[Apiv[i], j] = U[Apiv[i], j] - L[i,k]*U[Apiv[k],j]
            Q[Bpiv[i], j] = Q[Bpiv[i], j] - P[i,k]*U[Bpiv[k],j]


#The Equation we have is Ax - By + iBx + iAy = b + id
#So Ax-By = b and Bx + Ay = d (divided out the i)
#Well b and d will be given

b = array([(1, 2)]).reshape(2,1)
d = array([(3, 3)]).reshape(2,1)



Apivot = zeros((N,N))
Bpivot = zeros((N,N))
for b in range(0,N):
    Apivot[b, Apiv[b]] = 1
    Bpivot[b, Bpiv[b]] = 1
disp(Apivot)
disp(A)
disp(L)
transU = dot(Apivot, U)
disp(transU)