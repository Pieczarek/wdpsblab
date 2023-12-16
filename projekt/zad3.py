plik = 'zad2.txt'
with open(plik, 'r') as zad:
    liczby=zad.readlines()
    for licz in liczby:
        print(licz.strip())
        for i in range(0,len(liczby)):
            suma==0
            suma=int(licz.strip())+suma