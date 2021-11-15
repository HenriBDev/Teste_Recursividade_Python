from random import seed
from random import randint
import time
import sys
import numpy as np

sys.setrecursionlimit(10 ** 9)

def partition(colecao, l, h):
    i = ( l - 1 )
    x = colecao[h]
 
    for j in range(l, h):
        if   colecao[j] <= x:

            i = i + 1
            colecao[i], colecao[j] = colecao[j], colecao[i]
 
    colecao[i + 1], colecao[h] = colecao[h], colecao[i + 1]
    return (i + 1)
 
def quickSortIterative(colecao, l, h):
 
    size = h - l + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    while top >= 0:
 
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        p = partition( colecao, l, h )
 
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

def quickSortRecursive(colecao, low, high):
    if low < high:
 
        pi = partition(colecao, low, high)
 
        quickSortRecursive(colecao, low, pi-1)
        quickSortRecursive(colecao, pi + 1, high)

def criarColecao(colecao, tamanho):
     for indice in range(0, tamanho):
        valor = np.int64(randint(0, 51))
        colecao.append(valor)

def main():
    TAMANHO = 10000 
    colecao = []    
    criarColecao(colecao,  TAMANHO)

    colecaoRecursiva = colecao.copy()
    colecaoIterativa = colecao.copy()   
    tempoInicial = time.time() 
    quickSortRecursive(colecaoRecursiva, 0, TAMANHO - 1)
    tempoFinal = time.time()    
    print("Tempo Solução Recursiva: {} s".format(tempoFinal - tempoInicial))    
    tempoInicial = time.time() 
    quickSortIterative(colecaoIterativa, 0, TAMANHO - 1) 
    tempoFinal = time.time()
    print("Tempo Solução Iterativa: {} s".format(tempoFinal - tempoInicial))

if __name__ == '__main__' :
    main()