#include <stdio.h>

main()
{
	int x;
	double sum = 0;
	int cnt = 0;
	int number[100];
	scanf("%d",&x);
	while ( x != -1 ) {
		number[cnt] = x;
		cnt++;
		sum += x;
		scanf("%d",&x);
	}
	if (cnt>0) {
		printf("%f\n",sum/cnt);
		int i;
		for (i=0;i<cnt;i++) {
			printf("%d\n",number[i]);
		}
	}
	return 0;
}
