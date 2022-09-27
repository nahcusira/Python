def isPerfect( n ):
     
    # To store sum of divisors
    sum = 1
     
    # Find all divisors and add them
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n/i
        i += 1
     
    # If sum of divisors is equal to
    # n, then n is a perfect number
    
    return (True if sum == n and n!=1 else False)
 
# Driver program
while True:
    try:
        x = input()
        n = int(x)
        if n < 0:
            print("The number must be positive")
            continue
        for x in range (n):
            if isPerfect (x):
                print(x)
        break
    except ValueError:
        print("The number must be a positive number")
        continue

