#include <stdio.h>

int main(){
	int tamanho = 10, primeiro;
	int x[tamanho];
	int i;

	scanf("%d", &primeiro);

	for (i = 0; i < tamanho; i++){
		if (i == 0){
			x[i] = primeiro;
		} else {
			x[i] = x[i - 1] * 2;
		}
	}

	for (i = 0; i < tamanho; i++){
		printf("N[%d] = %d\n", i, x[i]);
	}
}