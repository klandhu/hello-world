#include <stdio.h>
main()
{
	int x;
	
	scanf("%d",&x);
	
	int i;
	//int isPrime =1; // x��������
	//int x=6;
	for (i=2;i<x;i++) {
		if (x % i == 0){
			//isPrime=0;
		}
	} 
//	if (isPrime==1){
	if (i==x) {
		printf("%d������",x);
	} 
	else
		{
			printf("%d��������",x);
		}
	
 
 } 
