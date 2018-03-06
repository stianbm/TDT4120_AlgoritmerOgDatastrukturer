#!/usr/bin/python3
from sys import stdin
#from string import ascii_lowercase as chars
from collections import deque

BASE = 26

def flexradix(A, d):
	lista = deque(A)
	
	for i in range(d,-1,-1):
		hauger = deque([deque() for _ in range(len(chars))])
		for string in lista:
			if len(string) > i:
				indeks = chars.index(string[i])
			else:
				indeks = 0
			hauger[indeks].append(string)

		lista = deque()
		for haug in hauger:
			lista.extend(haug)
	return lista



if __name__ == "__main__":
	main()
