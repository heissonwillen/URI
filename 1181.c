#include <stdio.h>

int main(){
	int dimensao = 12, cont = 0, linha;
	float matriz[dimensao][dimensao];
	float soma = 0;	

	int i, j;
	
	char c[1];
	
	scanf("%d", &linha);
	scanf("%s", &c);

	for (i = 0; i < dimensao; i++){
		for (j = 0; j < dimensao; j++){
			scanf("%f", &matriz[i][j]);
			if (i == linha){
				soma += matriz[i][j];	
				cont++;		
			}
		}
	}

	if (c[0]=='S'){
		printf("%.1f\n", soma);	
	} else if (c[0]=='M'){
		printf("%.1f\n", soma / cont);	
	}

	return 0;
}