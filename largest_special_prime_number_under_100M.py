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

#20INznpGzmkmK2NlZ0JILtO4OoYhOoYUB0OrOoTl5mJ3KgXrB0[8LTSSXUYhzUY8vmkyKUYevUYrDgYNK07yaf7soC3kKgMlOtHkLt[kZEclBtkyOoYwvtJGK2YevUY[v65iLtkeLEOhvtNlBtpizoY[v65yLdOkLEOhvtNlDn5lB07lOtJIDmllzmJ4vf7soCpiLdYIK0[eK27soleqO6keDpYp2CeH5d\F\fN6aQT6aQL[aQcUaQc[aQ57aQ5[aQDG
