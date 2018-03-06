#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    # SKRIV DIN KODE HER
		#As the input is read as a list of lists, recursion becomes hard to implement because one has to
		# keep track of whichstage one resides in. This results in iteration via double while loop.
		#The idea is to take two and two lists out of the main list, sort them into one, and append
		# this to the main list. When the main list has only one list, the task is complete.
		while len(decks) > 1:
			#Extract two lists, we know from the while condition there's at least two. Remove said list from
			# main list.
			List1 = decks[0]
			decks.remove(List1)
			List2 = decks[0]
			decks.remove(List2)
			#Allocate a list to store the sorted values
			SortedList = []
			#Implement iterators
			i = 0
			j = 0
			Lenght1 = len(List1)
			Length2 = len(List2)
			#Iterate
			while i < Lenght1 and j < Length2:
				if List1[i] < List2[j]:
					SortedList.append(List1[i])
					i += 1
				else:
					SortedList.append(List2[j])
					j += 1
			#When one list is empty, add the rest of the other list to SortedList, because they're sorted.
			SortedList.extend(List1[i:])
			SortedList.extend(List2[j:])
			#Add the SortedList to the main list
			decks.append(SortedList)
		#Return a more printable format, decks is at this time a list with a list, mainlist has one element
		LengthSorted = len(decks[0])
		Output = []
		k = 0
		while k < LengthSorted:
			Output.append(decks[0][k][1])
			k += 1
		return ''.join(Output)
		

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