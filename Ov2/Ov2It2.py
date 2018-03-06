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
			List1 = decks.pop(0)
			List2 = decks.pop(0)
			#Allocate a list to store the sorted values
			SortedList = []
			#Iterate
			while 0 < len(List1) and 0 < len(List2):
				if List1[0] < List2[0]:
					SortedList.append(List1.pop(0))
				else:
					SortedList.append(List2.pop(0))
			#When one list is empty, add the rest of the other list to SortedList, because they're sorted.
			SortedList.extend(List1)
			SortedList.extend(List2)
			#Add the SortedList to the main list
			decks.append(SortedList)
		return decks
		

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