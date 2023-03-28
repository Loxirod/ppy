def my_Panels(dlugosc,szerokosc,dlPanela,szPanela,ilosc):
    pole = dlugosc*szerokosc*1.1
    polePaneli=dlPanela*szPanela*ilosc
    iloscpaneli=1
    while(polePaneli<pole):
       # print("pole paneli: "+str(polePaneli))
        iloscpaneli+=1
        polePaneli+=dlPanela*szPanela*ilosc
    return iloscpaneli
#17.6
print("potrzeba: "+str(my_Panels(4,4,0.20,1,10)))


def is_prime(*n):
    for a in range(0, len(n)):
        jest_pierwsza=True
        for i in range(2, n[a]):
            if (n[a] % i) == 0:
                jest_pierwsza=False
                break
        if(jest_pierwsza):
            print("liczba: " + str(n[a]) + " jest pierwsza")
        else:
            print("liczba: " + str(n[a]) + " nie jest pierwsza")

is_prime(6,7,9)



def cezar(line,key):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z'] #25

    cezarLine=line.lower()
    list=''
    for letter in cezarLine:
        for x in alphabet:
            if (letter==x):
                while(alphabet.index(x) + key > len(alphabet)-1):
                    key-=len(alphabet)
               # print(alphabet.index(x)+key)
                #print(chr(97+alphabet.index(x)+key))
                list+=chr(97+alphabet.index(x)+key)

    print(list)
#a=97


cezar("HelloAZ",53)
