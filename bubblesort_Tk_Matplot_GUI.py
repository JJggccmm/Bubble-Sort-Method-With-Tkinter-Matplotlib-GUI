from tkinter import *
import matplotlib.pyplot as plt
    
##### IMPLEMENTACAO BASICA DO BUBBLE SORT #####
def BubbleSort(lista):
  #Variaveis auxiliares
  aux=0
  troca=True
  x=0
  
  while troca==True:
    troca=False
    #Utilizarei um for para percorrer a lista
    for x in range (lista):
      #Depois vamos fazer as comparaçoes dois a dois
      if lista[x] > lista[x+1]:
        lista[x+1],lista[x]=lista[x],lista[x+1]
        troca=troca+1
        troca=True
    #Podemos otimizar o algoritmo diminuindo o numero de comparaçoes a cada iteracao do for
   
