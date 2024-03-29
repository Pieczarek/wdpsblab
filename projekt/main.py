import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime
import csv


# Poprawność zadań: 8/11
# Dodatki: 1.5/2
# Znormalizowane: 0,7307692308

plik='liczby.txt'


def ex_1():
    for i in range(1,101):
        if i%15==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else:
            print(i)
def ex_2():
	n = int(input("Podaj dodatnia liczbe:"))

	with open(plik, 'w') as zad:
			for i in range(1,n+1):
				liczba=random.randint(1,100)
				zad.write(str(liczba)+'\n')
def ex_3():
	liczby=[]
	with open(plik, 'r') as zad:
		for licz in zad:
			liczby.append(int(licz.strip()))
			print (liczby)
		def srednia(nums):
			return sum(nums) / len(nums)
		def odch(nums):
			if len(nums) <= 1:
				return 0
			mean = srednia(nums)
			variance = sum((x - mean) ** 2 for x in nums) / len(nums)
			return variance ** 0.5

		def maximum(nums):
			return max(nums)

		def minimum(nums):
			return min(nums)

		print("Srednia:", srednia(liczby))
		print("Odchylenie standardowe:", odch(liczby))
		print("Maksimum:", maximum(liczby))
		print("Minimum:", minimum(liczby))

		sorted_numbers = sorted(liczby, reverse=True)
		print("Liczby malejaco:", sorted_numbers)
def ex_4(n):
	fibonacci=[]
	pierwsza=0
	druga=1
	for i in range(1,n+1):
		if i<=1:
			fibonacci.append(pierwsza)
			fibonacci.append(druga)
		else:
			nastepna=pierwsza+druga
			pierwsza=druga
			druga=nastepna
			fibonacci.append(nastepna)
	return fibonacci
			       
def ex_5():
	n = int(input("Ile liczb ciagu: "))
	fibo = ex_4(n)
	x_values = []
	for i in range(0, len(fibo)):
			x_values.append(i)
	y_values = fibo
	print(x_values, y_values)
	plt.plot(x_values, y_values)
	plt.title("Ciag Fibbonacciego")
	plt.show()

def ex_6():
	n=int(input("Ile wyrazow w slowniku:"))
	dict = {x: x ** 2 for x in range(1, n + 1)}
	print(dict)
	return dict


def ex_7():
	n=int(input("Ile wyrazow w slowniku:"))
	dict = {x: x ** 2 for x in range(1, n + 1)}
	suma = sum(dict.values())
	print(f"Suma wartości w słowniku: {suma}")
	return suma


def ex_8():
        for i in range(0,10):
            current_time = datetime.now()
            file_name = f"{current_time}.bin"  
            with open(file_name, "wb") as plik:
                for j in range(0,100):
                     plik.write(bytearray(random.randint(0,100)))



def ex_9():
    pass

def main():
		ex_1()
		ex_2()
		ex_3()
		ex_5()
		ex_6()
		ex_7()
		ex_8()
		ex_9()

if __name__ == '__main__':
    main()
