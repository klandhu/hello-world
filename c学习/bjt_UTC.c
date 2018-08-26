#include <stdio.h>
main()
{
	int bjt,utc,a,b;
	scanf("%d",&bjt);
	a = bjt /100;
	b = bjt % 100;
	a=a-8; 
	if (a>0)
	{
		utc = a*100 +b;
	} 
	else if (a==0)
	{
		utc=b;
	}
	else 
	{
		utc = (a+24)*100 +b;
	}
	
	printf("%d",utc);
 } 
