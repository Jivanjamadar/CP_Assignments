#include<stdio.h>
#include<stdbool.h>

//check no. is prime
bool prime(int num){
	if(num<=1) return false;
for (int i = 2; i * i <= num; ++i) {
        if (num % i == 0)
            return false;
    }
    return true;
}
void primeN(int N) {
    int cnt = 0;
    int num = 2;
    while (cnt < N+4) {
        if (prime(num)) {
            if (cnt % 2 == 0)
                printf("%d ", num);
            cnt++;
        }
        num++;
    }
}
int main(){
	int n;
	scanf("%d",&n);
	primeN(n);
	return 0;
}