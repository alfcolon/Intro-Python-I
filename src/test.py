import math
import time
import numpy as np
import sys


#z = np.arange(3, dtype=np.uint8)
#
#
#test = [np.uint8(1)] * (np.uint8(10))
#test2 = np.array([np.uint8(1)] * np.uint8(100), dtype='uint8')
#test2[0] = np.uint8(255)
##test.map(1, test)
#print(test2)
#print(test2[0])
#print(sys.getsizeof(test2[0]))
# 1. Create a sieve to hold odd numbers from 3 to potentialPrime

oneBillionOne = 1000000001
potentialPrime = oneBillionOne
oddNumberSieve = np.array([np.uint8(1)] * (potentialPrime / 2), dtype='uint8')
oddNumberSieve = [np.uint8] * ((potentialPrime / 2))


# 2. Loop through sieve of odd numbers
square_root = math.sqrt(potentialPrime)
def findPrimes():
    global potentialPrime
    global oddNumberSieve
    global square_root
    
    index = 0
    while index < square_root:
        sieveNumber = 3 + 2 * index
        # 3. Turn all numbers for which the sieveNumber is a composite to false
        jumpIndex = index + sieveNumber
        while jumpIndex < len(oddNumberSieve):
            if oddNumberSieve[jumpIndex] == 1 :
                if jumpIndex == len(oddNumberSieve) - 1:
                    return False
                oddNumberSieve[jumpIndex] = 0
            jumpIndex += sieveNumber
        # Optimizing by moving past false numbers
        index += 1
        while oddNumberSieve[index] == 0:
            index += 1
    return True

startTime = time.time()
isPrime = findPrimes()
endTime = time.time()
elapsedTime = endTime - startTime
print"That took %f seconds", elapsedTime
print("%d is prime is a %s statement!" %(potentialPrime, isPrime))







# I'm thinking about doing this in segments
# 1. Get the user input
#input_number_string = input("Enter number here to check if its prime.")

# 2. Convert input into a number
#input_number_int = int(input_number_string)
#
## 3. Create an array (list) of Bools set to true
#sieve = [True] * input_number_int
#
## 4. Set the first 2 values to false
#sieve[0] = False
#sieve[1] = False
#
#
## 5. Loop through numbers for 2...input_number_int time
#endRange = input_number_int
#square_root = math.sqrt(input_number_int)
#
#index = 2
#while index < square_root:
##    print("index:", index)
#    # 6. Turn all forward numbers that the index number is a multiple of to false
#    for index2  in range(index * 2, endRange, index):
#        if sieve[index2]:
#            sieve[index2] = False
#    # Optimizing moving past false numbers
#    index += 1
#    while sieve[index] == False:
#        index += 1
#
#
## 7. Print out whether the sieve[input_number] is true or not
#print(sieve[input_number_int - 1])


# 0.
#input_number_string = input("Enter number here to check if its prime.")
#
#input_number_int = int(input_number_string)
