#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge2(decks):
    # SKRIV DIN KODE HER
		#If only one element
			if len(decks) < 2:
				return decks
		#If not, divide in two lists and run reccursive
			else:
				MidPoint = int(len(decks)/2)
				List1 = merge(decks[:MidPoint])
				List2 = merge(decks[MidPoint:])
		#Combine the two lists
			#Variables
				ReturnDeck = []
				i = 0
				j = 0
			#Sort
				while i < len(List1) and j < len(List2):
					if List1[i] < List2[j]:
						ReturnDeck.append(List1[i])
						i += 1
					else:
						ReturnDeck.append(List2[j])
						j += 1
				ReturnDeck += List1[i:]
				ReturnDeck += List2[j:]
				return ReturnDeck

				
def merge3(deck):
	OutPut = merge2(deck)
	#Create output
	Letters = []
	k = 0
	while k < len(OutPut):
			Letters.append(OutPut[k][0])
			k += 1
	return Letters

	
def merge(deck):
	return len(deck)
	
	
def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()