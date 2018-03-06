#!/usr/bin/python3

from sys import stdin


class Node:
	def __init__(self):
		self.child = []
		self.ratatosk = False
		self.next_child = 0
		self.depth = 0	#Added


def dfs(root):
	# SKRIV DIN KODE HER
	#Copy paste bfs, men bruk FILO liste istedet
	#(bfs e bedre kommentert)
	nodeList = []
	nodeList.append(root)
	while len(nodeList) > 0:
		#Bruker FILO, pop'er derfor siste element
		#	i nodeList
		currentNode = nodeList.pop()
		if currentNode.ratatosk:
			return currentNode.depth
		for child in currentNode.child:
			child.depth = currentNode.depth + 1
			nodeList.append(child)
	return -1

def bfs(root):
	# SKRIV DIN KODE HER
	#Iterativ, legg nye noder i FIFO liste og
	#	iterer med while.
	#Lag en verdi i nodeklassen som holder 
	#	øye med dybde, sett den lik forelder
	#	sin +1 når ny node åpnes.
	#Antar Ratatosk alltid finnes i treet

	#FIFO liste over noder som skal traverseres
	#	legg til root i denne
	nodeList = []
	nodeList.append(root)
	while len(nodeList) > 0:
		#Fjern første node fra lista og lagre den
		#	i midlertidig sted
		currentNode = nodeList.pop(0)
		#Sjekk om node har Ratatosk, hvis ikke
		#	utvid barn, fiks dybde 
		if currentNode.ratatosk:
			return currentNode.depth
		for child in currentNode.child:
			child.depth = currentNode.depth + 1
			nodeList.append(child)
	#Hvis algoritmen ikke funker:
	return -1

function = stdin.readline().strip()
number_of_nodes = int(stdin.readline())
nodes = []
for i in range(number_of_nodes):
	nodes.append(Node())
start_node = nodes[int(stdin.readline())]
ratatosk_node = nodes[int(stdin.readline())]
ratatosk_node.ratatosk = True
for line in stdin:
	number = line.split()
	temp_node = nodes[int(number.pop(0))]
	for child_number in number:
		temp_node.child.append(nodes[int(child_number)])

if function == 'dfs':
	print(dfs(start_node))
elif function == 'bfs':
	print(bfs(start_node))
elif function == 'velg':
	# SKRIV DIN KODE HER
	#Kan finne måte å sjekke barn vs nivåer for
	#	å se om bfs(få nivåer) eller dfs(mange
	#	nivåer) er best
	#Se på antall noder og len(root.child) for å
	#	avgjøre
	if number_of_nodes / len(start_node.child) > 0.5:
		print(bfs(start_node))
	else:
		print(dfs(start_node))
	#Forbedra ikkje tid : /