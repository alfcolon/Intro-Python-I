#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <time.h>

void fill(char arr[], unsigned int size) {
	unsigned int index = 0;
	while(index < size) {
		arr[index] = 1;
		index += 1;
	}
}

bool findPrimes(char sieve[], unsigned int sieveSize, unsigned int potentialPrime) {
	unsigned int squareRoot = (unsigned int) sqrt(potentialPrime);	
	unsigned int index = 0;
	
	while (index < squareRoot) {
		unsigned int sieveNumber = 3 + 2 * index;
		unsigned int jumpIndex = index + sieveNumber;
		while(jumpIndex < sieveSize) {
			if (sieve[jumpIndex]) {
				if(jumpIndex == sieveSize - 1) {
					return false;
				}
				sieve[jumpIndex] = 0;
			}
			jumpIndex += sieveNumber;
		}
		index += 1;
		while (sieve[index] == 0) {
			index += 1;
		}
	}
	return true;
}
void	prime()
{
	unsigned int oneMillionOne = 1000001;
	unsigned int tenMillionOne = 10000001;
	unsigned int oneHundredMillionOne = 100000001;
	unsigned int oneBillionOne = 1000000001;
	unsigned int potentialPrime = oneBillionOne;
	unsigned int sieveSize = potentialPrime / 2;
	char	*sieve = malloc(sizeof(char) * sieveSize);
	clock_t start = clock();

	fill(sieve, potentialPrime / 2);
	bool isPrime = findPrimes(sieve, sieveSize, potentialPrime);	
	free(sieve);
	clock_t end = clock();
	float seconds = (float)(end - start) / CLOCKS_PER_SEC;
	printf("That took %f seconds\n", seconds);
	printf("%d is %s prime!", potentialPrime, isPrime ? "a" : "not a");
}	

int	main(void)
{
	prime();
	return (0);
}
