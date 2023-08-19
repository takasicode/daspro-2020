from MyLib import *

N = 0
while True:
    N = int(input("Panjang Array yang ingin diisi (1-100):"))
    if N > 0 and N <= 100:
        break
# input array T
x = [float]*N
print("---Input Array---")
for i in range(0,N) :
    x[i] = float(input("Indeks ke-"+str(i)+": "))

print("Sum array=",sumEL(N,x))
print("Avg array=",avgEL(N,x))
print("Med array=",medEL(N,x))
print("Min array=",minEL(N,x))
print("Max array=",maxEL(N,x))