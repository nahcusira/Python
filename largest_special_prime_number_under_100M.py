primes = []
import csv
with open("./prime-numbers.csv", 'r') as file:
		csvreader = csv.reader(file)
		for row in csvreader:
			for i in row:
				primes.append(int(i))
primes.sort(reverse=True)
for i in range(len(primes)):
	for j in range(i+1,len(primes)-1):
		if (primes[j] + primes[j + 1] + 1 == primes[i]):
			print(primes[i])