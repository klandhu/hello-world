#include <stdio.h>
int isPrime(int x, int kownPrimes[], int numberofknownPrimes);
 
int main()
{
	const int number = 10;
	int Prime[number] = {2};
	int count = 1;
	int i = 3;
	while ( count < number ) {
		if (isPrime(i, prime, count) ) {
			prime[count++] = i;
		} 
		{
			printf("i=%d \tcnt=%d\t",i,count);
			int i;
			for ( i=0; i<number; i++ ) {
				printf("%d\t", prime[i]);
			}
			printf("\n")
		}
		i++;
	} 
	for ( i=0;i<number;i++) {
		printf("%d",prime[i]]);
		if ( (i+1)%5 ) printf("\t");
		else printf("\n");
	}
	return 0;
 } 
