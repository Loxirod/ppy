x = "Python 2023"
y = x
z = x
print(x==y)
print(y==z)

print("x: " + str(type(x)) +" | "+ str(hex(id(x))) + "    y: " + str(type(y)) + " | "+ str(hex(id(y))) + "     z: " + str(type(z)) + " | "+ str(hex(id(z))) )

# ab again
z="Java 11"

print(x==y)
print(y==z)

print("x: " + str(type(x)) +" | "+ str(hex(id(x))) + "    y: " + str(type(y)) + " | "+ str(hex(id(y))) + "     z: " + str(type(z)) + " | "+ str(hex(id(z))) )


# zad 2

num1=input("podaj liczbe 1: ")
num2=input("podaj liczbe 2: ")
opperator=input("podaj znak")

match opperator:
    case '+': print(int(num1)+int(num2))
    case '-': print(int(num1)-int(num2))
    case '*': print(int(num1)*int(num2))
    case '/': print(int(num1)/int(num2))


text = ""
print("what is your name")
name = input("my name is: ")
print("")
print("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
print("a: oglądanie telewizji/filmów/seriali")
print("b: czytanie książek/czasopism")
odp1=input("c: inna: po prostu wpisz\n")

print("W jakich okolicznościach czytasz książki najczęściej?")
print("a: podczas podróży")
print("b: w czasie wolnym (po pracy, na urlopie)")
odp2=input("c: inna: po prostu wpisz\n")

print("Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? ")
print("a: chęć poszerzenia wiedzy")
print("b: czytanie mnie relaksuje/odpręża")
odp3=input("c: inna: po prostu wpisz\n")

print("Po książki w jakiej formie sięgasz najczęściej?")
print("a: papierowej (tradycyjnej)")
print("b: e-booki (książki elektroniczne) na komputerze")
odp4=input("c: inna: po prostu wpisz\n")

print("Ile książek czytasz średnio w ciągu roku? ")
print("a: 0")
print("b: 1")
odp5=input("c: inna: po prostu wpisz\n")

print("Jak często średnio czytasz książki?")
print("a: raz dziennie")
print("b: 2 razy w tygodniu")
odp6=input("c: inna: po prostu wpisz\n")

print("Po jakie gatunki książek sięgasz najczęściej?")
print("a: dramat")
print("b: Niemieckie Komedie Romantyczne")
odp7=input("c: inna: po prostu wpisz\n")














print("odpowiedzi:           ")
print(" ")
print("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
print(odp1)
if(odp1=="a"): print(" oglądanie telewizji/filmów/seriali")
if(odp1=="b"): print(" czytanie książek/czasopism")

print("\nW jakich okolicznościach czytasz książki najczęściej?")
print(odp2)
if(odp2=="a"):print(" podczas podróży")
if (odp2 == "b"):print(" w czasie wolnym (po pracy, na urlopie)")

print("\nJeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? ")
print(odp3)
if(odp3=="a"):print(" chęć poszerzenia wiedzy")
if (odp3 == "b"):print(" czytanie mnie relaksuje/odpręża")

print("\nPo książki w jakiej formie sięgasz najczęściej?")
print(odp4)
if(odp4=="a"):print(" papierowej (tradycyjnej)")
if (odp4 == "b"):print(" e-booki (książki elektroniczne) na komputerze")

print("\nIle książek czytasz średnio w ciągu roku? ")
print(odp5)
if(odp5=="a"):print(" 0")
if (odp5 == "b"):print(" 1")

print("\nJak często średnio czytasz książki?")
print(odp6)
if(odp6=="a"):print(" raz dziennie")
if (odp6 == "b"):print(" 2 razy w tygodniu")


print("\nPo jakie gatunki książek sięgasz najczęściej? ")
print(odp7)
if(odp7=="a"):print(" dramat")
if (odp7 == "b"):print(" Niemieckie Komedie Romantyczne")










