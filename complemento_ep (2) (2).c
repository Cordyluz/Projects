/* este foi o arquivo usado para fazer a biblioteca importada no Python*/
void selectionC(int *V, int n){
    // A função recebe um ponteiro de um vetor V e o tamanho n deste vetor
    // retornando este vetor ordenado com base no algoritmo Selection Sort
    int j, i, tmp;
    j = i = 0;
    while (j < n - 1){
        i = j + 1;
        while(i < n){
            if (*(V+j) > *(V+i)){
                tmp = *(V+j);
                *(V+j) = *(V+i);
                *(V+i) = tmp;
            }
            i = i + 1;
    }
        j = j + 1;
    }
}

void bubbleC(int *V, int n){
    // A função recebe um ponteiro de um vetor V e o tamanho n deste vetor
    // retornando este vetor ordenado com base no algoritmo Bubble Sort
    int troca;
    troca = 0;
    int i, j, tmp;
    while(n > 0){
        j = 0;
        i = 1;
        while(i < n){
            if(*(V+j) > *(V+i)){
                tmp = *(V+j);
                *(V+j) = *(V+i);
                *(V+i) = tmp;
                troca = 1;
            }
            i = i + 1;
            j = j + 1;
        }
                                    
        n = n - 1;
        if(troca == 0){
            n = 0;
        }
    }
}



void insertionC(int *V, int n){
    // A função recebe um ponteiro de um vetor V e o tamanho n deste vetor
    // retornando este vetor ordenado com base no algoritmo Insertion Sort
    int k, i, j, tmp;
    k = 1;
    while(k < n){
        i = k;
        j = i - 1;
        while(i > 0){
            
            if (*(V+i) >= *(V+j)){
                i = 0;
            }
            else{
                tmp = *(V+i);
                *(V+i) = *(V+j);
                *(V+j) = tmp;
            }
            i = i - 1;
            j = i - 1;
        }
        k = k + 1;
    }
}

void countingC(int *V, int n){
    // A função recebe um ponteiro de um vetor V e o tamanho n deste vetor
    // retornando este vetor ordenado com base no algoritmo Counting Sort

    int a, b, j, valorMax;
    a = b = j = valorMax = 0;

    for (int k = 0; k < n; k++){
        if (valorMax < V[k]){
            valorMax = V[k];
        }
    }
    int H[valorMax];
    for (int l = 0; l < valorMax; l++){
        H[l] = 0;
    }
    while (j < n){
        H[*(V+j)] = H[*(V+j)] + 1;
        j = j + 1;
    }
    while(a < n){
        
        if (H[b] > 0){
            V[a] = b;
            a = a + 1;
            H[b] = H[b] - 1;
        }
        else{
            b = b + 1;
        }
    }
}