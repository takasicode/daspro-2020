#Kamus
n = int(input()) 

#Algoritma    
for i in range(n):
    t = int(input())
    for num in range(t+1):
        for j in range(num):
            print (num, end=" ")
        print("\n")