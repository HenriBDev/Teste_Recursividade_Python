from random import seed
from random import randint
import time
from datetime import datetime
import sys
import os
import numpy as np
import pandas as pd
from pandas.io.sql import pandasSQL_builder
 
def quickSortIterable(colecao, l, h):
 
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

def predefinedTest(resultsDict, multiplyBy2 = True, collectionSize = 5):
    
    if multiplyBy2:
        collectionSize *= 2
    else:
        collectionSize *= 5
    multiplyBy2 = not multiplyBy2

    if (collectionSize <= 10000):
        resultsDict = testPerformance(collectionSize, resultsDict)
        return predefinedTest(resultsDict, multiplyBy2, collectionSize)
    else:
        return resultsDict

def testPerformance(collectionSize, resultsDict):

    print(f"Testando lista com {collectionSize} itens. . .")

    resultsDict["MOMENTO_REALIZADO"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    resultsDict["TAMANHO_LISTA"].append(collectionSize)
    collection = createCollection(collectionSize)

    initialTime = time.time() 
    quickSortRecursive(collection, 0, collectionSize - 1)
    finalTime = time.time()
    resultsDict["TEMPO_RECURSIVA"].append(f"{round(finalTime - initialTime,4)}s")

    initialTime = time.time() 
    quickSortIterable(collection, 0, collectionSize - 1) 
    finalTime = time.time()
    resultsDict["TEMPO_ITERAVEL"].append(f"{round(finalTime - initialTime,4)}s")

    return resultsDict

def showResults(resultsDict):
    print("Veja os resultados:\n")
    print(pd.DataFrame.from_dict(resultsDict))
    input("\nPressione enter para continuar. . .")

def main():

    resultsDict = {"MOMENTO_REALIZADO": [],
                   "TAMANHO_LISTA": [],
                   "TEMPO_ITERAVEL": [],
                   "TEMPO_RECURSIVA": []}

    print("Bem-vindo ao sistema de teste de perfomance: Recursividade X Iteração\n" +
          "Neste teste será executado duas funções Quicksort em uma list contendo diversos itens, uma delas percorre a list de forma recursiva, enquanto a outra faz isso de forma iterativa\n" +
          "Os resultados serão relatados após o teste")

    while True:
        os.system("CLS")
        print("1 - Realizar teste pré-definido (10 até 10000 itens)\n" +
              "2 - Realizar teste com um número selecionado de itens\n" +
              "3 - Ver resultado dos testes\n" +
              "4 - Exportar resultados em uma planilha (.xlsx)\n" +
              "5 - Exportar resultados em um arquivo de texto (.csv)\n" +
              "6 - Limpar resultados\n" +
              "7 - Sair\n")

        selection = int(input("Escolha: "))
        if (selection < 1 or selection > 7):
            print("Escolha inválida! Selecione um número entre 1 e 7")
            input("Pressione enter para continuar. . .")
        else:
            os.system("CLS")
            if (selection == 1):
                resultsDict = predefinedTest(resultsDict)
                showResults(resultsDict)
            elif (selection == 2):
                qtyItems = int(input("Digite a quantidade de itens da list: "))
                if (sys.getrecursionlimit() < qtyItems):
                    sys.setrecursionlimit(qtyItems)
                resultsDict = testPerformance(qtyItems, resultsDict)
                showResults(resultsDict)
            elif (selection == 3):
                if(resultsDict["TAMANHO_LISTA"] != []):
                    showResults(resultsDict)
                else:
                    input("Ainda não foi realizado nenhum teste.\nPressione enter para continuar. . .")
            elif (selection == 4):
                resultsDataFrame = pd.DataFrame.from_dict(resultsDict)
                resultsDataFrame.to_excel(f"{input('Digite o nome do arquivo: ')}.xlsx")
                input("Arquivo gerado com sucesso!\nPressione Enter Para Continuar. . .")
            elif (selection == 5):
                resultsDataFrame = pd.DataFrame.from_dict(resultsDict)
                resultsDataFrame.to_csv(f"{input('Digite o nome do arquivo: ')}.csv")
                input("Arquivo gerado com sucesso!\nPressione Enter Para Continuar. . .")
            elif (selection == 6):
                while True:
                    confirm = input("Tem certeza que deseja apagar os resultados? [S/N]\nEscolha: ").upper()
                    os.system("CLS")
                    if (confirm == "S" or confirm == "N"):
                        if (confirm == "S"):
                            resultsDict = {"MOMENTO_REALIZADO": [],
                                           "TAMANHO_LISTA": [],
                                           "TEMPO_RECURSIVA": [],
                                           "TEMPO_ITERAVEL": []}
                            input("Dados apagados com sucesso!\nPressione enter para continuar...")
                        break
            else:
                break

    print("Obrigado por usar o sistema!")
    
if  __name__ == '__main__' :
    main()