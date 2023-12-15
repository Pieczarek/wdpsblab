n = int(input("Podaj liczba"))
for i in range(1,n+1):
    if i<=1:
        pierwsza=0
        druga=1
        nastepna=1
        print(pierwsza)
        print(druga)
    else:
        nastepna=pierwsza+druga
        pierwsza=druga
        druga=nastepna
        print(nastepna)
        