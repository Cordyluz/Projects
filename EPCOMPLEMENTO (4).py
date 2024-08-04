
import ctypes
libsort = ctypes.CDLL("./libsortings.so")
libsort.selectionC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.bubbleC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.insertionC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.countingC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

def selectionC(V,n):
    pV = (ctypes.c_int *n)(*V)
    libsort.selectionC(pV,n)
    
def bubbleC(V,n):
    pV = (ctypes.c_int *n)(*V)
    libsort.bubbleC(pV,n)
    
def insertionC(V,n):
    pV = (ctypes.c_int *n)(*V)
    libsort.insertionC(pV,n)
    
def countingC(V,n):
    pV = (ctypes.c_int *n)(*V)
    libsort.countingC(pV,n)
#O acima importa a biblioteca feita em C e define as funções de ordenação para serem usadas no experimento

from sys import platform
import time as T
import matplotlib.pyplot as plt
from random import randint
import copy



#A biblioteca copy foi importada para o uso da função deepcopy em listas de 
#listas, pois acabei percebendo que o comando list não funciona para este caso

def counting(V,n):
    '''O argumento V representa um vetor desordenado e o argumento n o tamanho 
    desse vetor, função retorna um vetor ordenado pelo método Counting Sort
    '''
    H = [0]
    a = b = i = j = 0

    while (i < max (V)):
        H.append(0)
        i = i + 1
        
    while (j < n):
        H[V[j]] = H[V[j]] + 1
        j = j + 1

    while(a < n):
        
        if (H[b] > 0):
            V[a] = b
            a = a + 1
            H[b] = H[b] - 1
        else:
            b = b + 1

    return V
    

def GraficaSortings(mpontos,mediaMCMPi,desvioMCMPi,tipo_sort):
    '''essa função recebe m pontos da simulação, a média dos valores e o 
    desvio dos valores, e o tipo de ordenação,
    retornando parâmetros para os gráficos salvos na main
    '''
    #note que o argumento adicionado é usado abaixo para nomear cada tipo de
    #ordenação no gráfico
    x = mpontos
    y = mediaMCMPi
    d = desvioMCMPi
    if(tipo_sort == selectionC):
        plt.errorbar(x,y,yerr=d,fmt='o', label='selectionC')
    elif(tipo_sort == bubbleC):
        plt.errorbar(x,y,yerr=d,fmt='o', label='bubbleC')
    elif(tipo_sort == insertionC): 
        plt.errorbar(x,y,yerr=d,fmt='o', label='insertionC')
    elif(tipo_sort == countingC):
        plt.errorbar(x,y,yerr=d,fmt='o', label='countingC')
    elif(tipo_sort == counting):
        plt.errorbar(x,y,yerr=d,fmt='o', label='counting')
    elif(tipo_sort == 0):
        plt.errorbar(x,y,yerr=d,fmt='o', label='Timsort')
        plt.title("Experimento com C")
        plt.xlabel("Tamanho dos vetores ordenados")
        plt.ylabel("Tempo gasto para ordená-los")
        plt.legend()
        plt.show()
        plt.savefig('IMG2')
        plt.clf()

def mediaT(T,n):
    '''essa função recebe um vetor T e seu tamanho n, retornando a média 
    aritmética dos valores deste vetor
    '''
    total = 0
    for i in range (n):
        total = total + T[i]
    media = total / n 
    return media
    


def varT(T,n):
    '''essa função recebe um vetor T e seu tamanho n, retornando a variância
    populacional dos valores do vetor T
    '''
    media = mediaT(T,n)
    a = 0
    for i in range (n):
        a = a + (T[i] - media)**2
    var = a / n
    return var



def timeMe(func,V,n,m,p):
    ''' Essa função recebe uma função de Sort, no caso o Tim Sort sendo 
    considerado como 0, uma lista de listas V com seus elementos sendo vetores
    a serem ordenados, o tamanho n desses vetores,
    uma quantia m de repetições e um percentual p de desordenação,
    retornando um valor da média de tempo para a ordenação dos vetores de V
    e um valor da variância do tempo de ordenação destes mesmos vetores
    '''
    #Note que o percentual p não foi usado nessa função pois estava causando
    #um excesso de erros, devido a cópia de lista de listas
    #que foi consertada usando a função deepcopy da biblioteca copy
    #e o embaralhamento na própria main()
    reps = m
    tempos = []
    if (func == 0):
        while(m > 0):
            start = T.process_time()
            V[m-1].sort()
            finish = T.process_time()
            Vptime = finish - start
            tempos.append(Vptime)
            m = m - 1
    #o if define o loop acima para o TimSort
    else: 
        while(m > 0):
            start = T.process_time()
            func(V[m-1],n)
            finish = T.process_time()
            Vptime = finish - start
            tempos.append(Vptime)
            m = m - 1
    #o else define o loop para execução dos outros algoritmos de ordenação

    print (tempos, reps)
    media = mediaT(tempos, reps)
    print (media)
    var = varT(tempos, reps)
    print (var)
    return [media, var]
    
def main():
    tamanho = [1000, 5000, 10000, 50000, 100000]
    #acima estão definidos os tamanhos para o experimento 1
    selectionC_medias = []
    selectionC_vars = []
    bubbleC_medias = []
    bubbleC_vars = []
    insertionC_medias = []
    insertionC_vars = []
    countingC_medias = []
    countingC_vars = []
    counting_medias = []
    counting_vars = []
    timsort_medias = []
    timsort_vars = []
    #acima estão definidos vetores para armazenar os resultados das ordenações
    #pela função timeMe, onde sort_medias indica medias de tempo e 
    #sort_vars indica variâncias de tempo
    
    for w in range (5):
        H = []
        for j in range (10):
            V = [randint(0,9999) for i in range (tamanho[w])]
            H.append(V)
        #o loop acima cria as sub-listas de H ordenadas aleatoriamente
        V = copy.deepcopy(H)
        M, V = timeMe(selectionC,V,tamanho[w],10,0)
        selectionC_medias.append(M)
        selectionC_vars.append(V)
        
        V = copy.deepcopy(H)
        M, V = timeMe(bubbleC,V,tamanho[w],10,0)
        bubbleC_medias.append(M)
        bubbleC_vars.append(V)
        
        V = copy.deepcopy(H)
        M, V = timeMe(insertionC,V,tamanho[w],10,0)
        insertionC_medias.append(M)
        insertionC_vars.append(V)
        
        V = copy.deepcopy(H)
        M, V = timeMe(countingC,V,tamanho[w],10,0)
        countingC_medias.append(M)
        countingC_vars.append(V)
        
        V = copy.deepcopy(H)
        M, V = timeMe(counting,V,tamanho[w],10,0)
        counting_medias.append(M)
        counting_vars.append(V)
        
        V = copy.deepcopy(H)
        M, V = timeMe(0,V,tamanho[w],10,0)
        timsort_medias.append(M)
        timsort_vars.append(V)
        
    #acima está o loop que roda as funções sempre antes usando o comando
    #deepcopy para copiar a lista de listas H em V, de modo a que uma alteração
    #nas listas internas de V não troque as listas internas de H
    for i in range(len(selectionC_vars)):
        selectionC_vars[i] = selectionC_vars[i]**0.5
        bubbleC_vars[i] = bubbleC_vars[i]**0.5
        insertionC_vars[i] = insertionC_vars[i]**0.5
        countingC_vars[i] = countingC_vars[i]**0.5
        counting_vars[i] = counting_vars[i]**0.5
        timsort_vars[i] = timsort_vars[i]**0.5
    #o loop acima calcula os desvios padrões
        
    GraficaSortings(tamanho,selectionC_medias,selectionC_vars,selectionC)
    GraficaSortings(tamanho,bubbleC_medias,bubbleC_vars,bubbleC)
    GraficaSortings(tamanho,insertionC_medias,insertionC_vars,insertionC)
    GraficaSortings(tamanho,countingC_medias,countingC_vars,countingC)
    GraficaSortings(tamanho,counting_medias,counting_vars,counting)
    GraficaSortings(tamanho,timsort_medias,timsort_vars,0)
    #as funções acima adicionam os parâmetros para a formação do gráfico
    

main()