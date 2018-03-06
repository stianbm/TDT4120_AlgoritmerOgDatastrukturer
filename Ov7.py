from sys import stdin

Inf = 1000000000


#Returner minst av to int
def Min(q,t):
	if q < t:
		return q
	else:
		return t


#Lokalt optimalitet er at man alltid velger høyest mulig mynt
def min_coins_greedy(coins, value):
# SKRIV DIN KODE HER
	if value == 0:
		q = 0
	else:
		MaxCoin = -Inf
		for mynt in coins:
			if mynt <= value and mynt > MaxCoin:
				MaxCoin = mynt
		q = 1 + min_coins_greedy(coins, value - MaxCoin)
	return q


def min_coins_dynamic(coins, value):
# SKRIV DIN KODE HER
#Initialiser problem, lagre mellomlagringer i liste som sendes videre
#	til rekursiv funksjon.
#Lag mellomlagringsliste
	Svar = []
	for i in range(0, value + 1):
		Svar.append(-Inf)
	return Aux(coins, value, Svar)
	
	
#Sjekker først om svaret er funnet før, hvis ikke finner den svaret
#	rekursivt basert på pinnekutting
def Aux(coins, value, Svar):
	if Svar[value] >= 0:
		q = Svar[value]
	elif value == 0:
		q = 0
	else:
		q = Inf
		for mynt in coins:
			if mynt <= value:
				t = 1 + Aux(coins, value - mynt, Svar)
				q = Min(q,t)
		Svar[value] = q
	return q


def can_use_greedy(coins):
# bare returner False her hvis du ikke klarer aa finne ut
# hva som er kriteriet for at den graadige algoritmen skal fungere
# SKRIV DIN KODE HER
	return False
	

coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        print(min_coins_greedy(coins, int(line)))
else:
    for line in stdin:
        print(min_coins_dynamic(coins, int(line)))