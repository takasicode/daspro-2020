def tampilDenganSpasi (kata, split=True) :
    kata=list(kata)
    if split :
        kata = " ".join(kata)
    else :
        kata = "-".join(kata)
    return kata

Kata1 = tampilDenganSpasi("SEMANGAT")
Kata2 = tampilDenganSpasi("SEMANGAT", False)

print(Kata1)
print(Kata2)