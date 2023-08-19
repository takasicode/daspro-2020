#Algoritma
ipk=float(input("masukan ipk"))
if ((ipk>=0) and (ipk<=4.0)) :
    if (ipk>=3.5) :
        print ("Dengan pujian/Cumlaude")
    elif (ipk>=3.0 and (ipk<3.5)) :
        print ("Sangat memuaskan?Very Good")
    elif (ipk>=2.75 and (ipk<3.0)) :
        print ("Memuaskan/Good")
else :
    print ("ipk tidak valid")