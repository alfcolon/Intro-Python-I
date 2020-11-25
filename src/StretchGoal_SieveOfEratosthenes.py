import math
import time

def findPrimes( potentialPrime ):
    # 0. Return early if number is even
    if potentialPrime & 1 == 0:
        return False
    # 1. Create a sieve to hold odd numbers from 3 to potentialPrime
    oddNumberSieve = [True] * int((potentialPrime / 2))
    
    # 2. Loop through sieve of odd numbers
    square_root = math.sqrt(potentialPrime)
    index = 0
    while index < square_root:
        sieveNumber = 3 + 2 * index
        # 3. Turn all numbers for which the sieveNumber is a composite to false
        jumpIndex = index + sieveNumber
        while jumpIndex < len(oddNumberSieve):
            if oddNumberSieve[jumpIndex]:
                if jumpIndex == len(oddNumberSieve) - 1:
                    return False
                oddNumberSieve[jumpIndex] = False
            jumpIndex += sieveNumber
        # Optimizing by moving past false numbers
        index += 1
        while oddNumberSieve[index] == False:
            index += 1
    return True

# 1. Get the user input
input_number_string = input("Enter number here to check if its prime.")

# 2. Convert input into a number
potentialPrime = int(input_number_string)

# 3. Print false if its even else check if its prime
startTime = time.time()
isPrime = findPrimes(potentialPrime)
endTime = time.time()
elapsedTime = endTime - startTime

print("That took", elapsedTime, "seconds")
print("%d is prime is a %s statement!" %(potentialPrime, isPrime))
