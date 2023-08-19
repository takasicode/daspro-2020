def sumEL(N,T) :
    sL=0
    for i in range(0,N) :
        sL+=T[i]
    return sL

def avgEL(N,T) :
    return sumEL(N,T) /N

def medEL(N,T) :
    t = [float]*N
    for i in range(0,N) :
        t[i]=T[i]
    t=sorted(t)
    print("Sorted T=",t)
    if len(t)%2==1:
        return t[int((N/2))]
    else:
        return (t[int((N/2))]+t[int((N/2))-1])/2

def minEL(N,T) :
    min=T[0]
    for i in range(1,N) :
        if T[i]<min:
            min=T[i]
    return min

def maxEL(N,T) :
    max=T[0]
    for i in range(1,N) :
        if T[i]> max:
            max=T[i]
    return max