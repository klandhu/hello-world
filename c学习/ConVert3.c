#include <stdio.h>
main()
{
	int zs,a,b,c;
	scanf("%d",&zs);
	a = zs / 100;
	b = zs % 10;
	c = zs / 10 % 10 ;
	printf("%d",b*100+c*10 +a);
	
	
}
