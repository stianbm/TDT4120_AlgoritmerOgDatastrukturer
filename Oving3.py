#!/usr/bin/python3

from sys import stdin


def sort_list(A):
    # NOTICE: The sorted list must be returned.
	#Use quicksort, pivot over first element.
	if len(A) < 1:
		#Return list if empty
		return A
	else:
		#Two lists to use recursively
		LessList = []
		GreatList = []
		#Save pivot in list of one element to ease the return
		Pivot = []
		Pivot.append(A[0])
		#Remove pivot from list
		for Element in A[1:]:
			if Element <= Pivot[0]:
				LessList.append(Element)
			else:
				GreatList.append(Element)
		return sort_list(LessList)+Pivot+sort_list(GreatList)


def find(A, lower, upper):
    # NOTICE: The result must be returned.

    k = 0
    l = 0
    maxvalue = A[-1]
    minvalue = A[0]
    minmax = []

    for Element in A[0:]:

        if Element <= lower:
            k = Element
            if k > minvalue:
                minvalue = k

        elif Element >= upper:
            l = Element
            if l < maxvalue:
                maxvalue = l

    minmax.append(minvalue)
    minmax.append(maxvalue)

    return minmax








def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()