import random as rand
plik="zad2.txt"

n = int(input("Podaj dodatnia liczbe:"))
while (n<1):
    n = int(input("Podaj dodatnia liczbe:"))
    if n>1:
        break
with open(plik, 'w') as zad:
    for i in range(1,n+1):
        liczba=rand.randint(1,100)
        zad.write(str(liczba)+'\n')
    