L=[]
def maxEL() :
    global L
    if len(L)>0:
        max=L[0]
        for i in L:
            if i>max:
                max=i
    return max

def minEL() :
    global L
    if L is not None:
        min=L[0]
        for i in L:
            if i<min:
                min=i
    return min

def medEL() :
    global L
    l=sorted(L)
    print("Sorted L=",l)
    if l is not None:
        if len(l)%2==1: #ganjil
            return l[int((len(l)/2))]
        else: #genap
            return (l[int((len(l)/2))]+l[int((len(l)/2))-l])/2

def avgEL():
    global L
    l=0
    if L is not None:
        for i in L:
            l+=i
    return sumEL()/l

def sumEL():
    global L
    sL=0
    if L is not None:
        for i in L:
            sL+=i
    return sL

def main():
    i=1
    global L
    while True:
        el=float(input("masukkan elemen list ke-"+str((i))+":"))
        if el==0:
            break
        else:
            L.append(el)
        i+=1

    print("L", L)
    print("sum L=",sumEL())
    print("avg L=",avgEL())
    print("med L=",medEL())
    print("min L=",minEL())
    print("max L=",maxEL())

if __name__ == "__main__":
    main()