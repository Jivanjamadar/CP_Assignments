#include<stdio.h>
#include<math.h>
int main(){
	int n[3];
	for(int i=0;i<3;i++){
		scanf("%d",&n[i]);
	} int z=pow(n[0],n[1]);
	int m=(z%n[2]);
	printf("%d",m);
	return 0;
}