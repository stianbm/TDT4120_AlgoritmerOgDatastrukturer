#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge2(decks):
    # SKRIV DIN KODE HER
		while len(decks) > 1:
			s1 = decks.pop(0)
			s2 = decks.pop(0)
			s = []
			while len(s1) > 0 and len(s2) > 0:
				if s1[0] < s2[0]:
					s.append(s1.pop(0))
				else:
					s.append(s2.pop(0))
			s.extend(s1)
			s.extend(s2)
			decks.append(s)
		letters = []
		for (number, letter) in decks[0]:
			letters.append(letter)
		return ''.join(letters)
				

				
def merge(decks):
	return decks[1][1]
	
	
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