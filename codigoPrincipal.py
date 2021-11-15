from random import seed
from random import randint
import time
import sys
import numpy as np
import pandas as pd
 
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

def partition(colecao, low, high):
    i = (low - 1)        
    pivot = colecao[high]    
 
    for j in range(low, high):
        if colecao[j] <= pivot:
            i += 1
            colecao[i], colecao[j] = colecao[j], colecao[i]
 
    colecao[i + 1], colecao[high] = colecao[high], colecao[i + 1]
    return (i + 1)
 
def quickSortRecursive(colecao, low, high):
    if low < high:
 
        pi = partition(colecao, low, high)
 
        quickSortRecursive(colecao, low, pi-1)
        quickSortRecursive(colecao, pi + 1, high)

def createCollection(size):
    collection = []
    for index in range(0, size):
        value = np.int64(randint(0, 51))
        collection.append(value)
    return collection

def testPerformance(multiplyBy5, collectionSize, recursiveResults = [], iterativeResults = [], sizesCollection = []):
    if collectionSize <= 10000:

        print(f"Testando lista com {collectionSize} itens. . .")
        
        sizesCollection.append(collectionSize)
        collection = createCollection(collectionSize)

        initialTime = time.time() 
        quickSortRecursive(collection, 0, collectionSize - 1)
        finalTime = time.time()
        recursiveResults.append(f"{round(finalTime - initialTime,4)}s")

        initialTime = time.time() 
        quickSortIterative(collection, 0, collectionSize - 1) 
        finalTime = time.time()
        iterativeResults.append(f"{round(finalTime - initialTime,4)}s")

        multiplyBy5 = not multiplyBy5
        if multiplyBy5:
            collectionSize *= 5
        else:
            collectionSize *= 2

        testPerformance(multiplyBy5, collectionSize, recursiveResults, iterativeResults)

    else:
        print("Ok!\n\nVeja os resultados:\n")

        dictResults = {"TAMANHO_LISTA": sizesCollection, "TEMPO_RECURSIVA": recursiveResults, "TEMPO_ITERATIVA": iterativeResults}
        dataFrame_Results = pd.DataFrame.from_dict(dictResults)
        print(dataFrame_Results)

def main():
    testPerformance(False, 10)
    
if  __name__ == '__main__' :
    main()