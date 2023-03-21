import random
import getpass
liczby = input("podaj liczby rozdzielone przecinkiem")

liczbaList = liczby.split(",")
liczbaMin = liczby[0]

for i in range(0, len(liczbaList)):
    if liczbaMin > liczbaList[i]:
        liczbaMin = liczbaList[i]

print(liczbaMin)

cities = "Warszawa,Kraków,Wrocław,Łódź,Poznań,Gdańsk,Szczecin,Bydgoszcz,Lublin,Białystok"
citieslist = cities.split(",")
for i in range(0, 10):
    randomNum = random.randint(0, len(citieslist)-1)
    print(citieslist[randomNum])
    citieslist.pop(randomNum)



print("\n\n\n\n\n")

wybor=int(input("wybiez tryb gry: \n1.AI 2.hotseats"))
liczbaRund=int(input("wybiez liczbe rund"))
gracz1=0
gracz2=0# w 1 rundzie wygral ... itp
listaWygranych=[]

temp=0
while temp!=liczbaRund:

    if wybor == 1:
        print("JESTES GRACZEM 1 \n AI FIGHT::::::::::::::::: ")
        wybor1 = int(getpass.getpass("wybierz 1.papier 2.kamieen 3.destroyer3000(nozyce)"))
        wybor2 = int(random.randint(1,4))
        if wybor1 == wybor2:
            print("remis")
        if wybor1 == 1 and wybor2 == 2:  # papier i kamien
            print("wyrgywa gracz 1")
            gracz1 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 1")
        if wybor1 == 2 and wybor2 == 1:
            print("wyrgywa gracz 2")
            gracz2 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 2")

        if wybor1 == 1 and wybor2 == 3:
            print("wyrgywa gracz 2")
            gracz2 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 2")
        if wybor1 == 3 and wybor2 == 1:
            print("wyrgywa gracz 1")
            gracz1 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 1")

        if wybor1 == 1 and wybor2 == 3:  # papier i nozyce
            print("wyrgywa gracz 2")
            gracz2 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 2")
        if wybor1 == 3 and wybor2 == 1:
            print("wyrgywa gracz 1")
            gracz1 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 1")

        if wybor1 == 2 and wybor2 == 3:  # kamien i nozyce
            print("wyrgywa gracz 1")
            gracz1 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 1")
        if wybor1 == 3 and wybor2 == 2:
            print("wyrgywa gracz 2")
            gracz2 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 2")
        temp += 1

    if wybor == 2:
        print("czekam")
        wybor1 = int(getpass.getpass("wybierz 1.papier 2.kamieen 3.destroyer3000(nozyce)"))
        wybor2 = int(getpass.getpass("wybierz 1.papier 2.kamieen 3.destroyer3000(nozyce)"))
        if wybor1==wybor2:
            print("remis")
        if wybor1==1 and wybor2==2: # papier i kamien
            print("wyrgywa gracz 1")
            gracz1+=1
            listaWygranych.append("Round: "+str(temp)+" wygral gracz 1")
        if wybor1==2 and wybor2==1:
            print("wyrgywa gracz 2")
            gracz2 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 2")


        if wybor1 == 1 and wybor2 == 3: # papier i nozyce
            print("wyrgywa gracz 2")
            gracz2 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 2")
        if wybor1 == 3 and wybor2 == 1:
            print("wyrgywa gracz 1")
            gracz1 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 1")

        if wybor1 == 2 and wybor2 == 3: # kamien i nozyce
            print("wyrgywa gracz 1")
            gracz1 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 1")
        if wybor1 == 3 and wybor2 == 2:
            print("wyrgywa gracz 2")
            gracz2 += 1
            listaWygranych.append("Round: " + str(temp) + " wygral gracz 2")
        temp+=1


print(listaWygranych)
print("punkty gracza 1: "+str(gracz1)+"\n"+ "punkty gracza 2: "+str(gracz2))