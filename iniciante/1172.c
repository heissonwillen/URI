#include <stdio.h>

int main(){
	int tamanho = 10;
	int x[tamanho];
	int i;

	for (i = 0; i < tamanho; i++){
		scanf("%d", &x[i]);
		if (x[i] <= 0){
			x[i] = 1;
		}
	}

	for (i = 0; i < tamanho; i++){
		printf("X[%d] = %d\n", i, x[i]);
	}
}