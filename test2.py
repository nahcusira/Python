primes = []
import csv
with open("./a - Copy.csv", 'r') as file:
		csvreader = csv.reader(file)
		for row in csvreader:
			for i in row:
				if int(i) >20000000:
					primes.append(int(i))
primes.sort(reverse=True)
for i in range(len(primes)):
	for j in range(len(primes)-i-1):
		if (primes[j] + primes[j + 1] + 1 == primes[i]):
			print(primes[i])
			break;