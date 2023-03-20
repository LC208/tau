T1 = 0.1
T2 = 0.28284
T3= 0.8
k = 17

C11 = T1*T2*T3
C12 = T1+T2+T3
C21 = T1*T2+T2*T3+T3*T1
C22 =1+ k
r3 = C11/C21
C31 = C12 - r3*C22
r4 = C21/C31
C41 = C22 - r4*0
print('C11:' , C11)
print('C12:' , C12)
print('C21:' , C21)
print('C22:' , C22)
print('C31:' , C31)
print('C41:' , C41)
