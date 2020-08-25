#include <stdio.h>

int main(){
	int tamanho = 100;
	float x[tamanho];
	int i;

	for (i = 0; i < tamanho; i++){
		scanf("%f", &x[i]);
	}

	for (i = 0; i < tamanho; i++){
		if (x[i] <= 10){
			printf("A[%d] = %.1f\n", i, x[i]);
		}
	}
}