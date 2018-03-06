#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    result = []
    length1 = len(decks) #size of list

    for i in range (0,length1):
        length2 = len(decks[i])

        for j in range (0,length2):
            result.append(decks[i][j])
    return result






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