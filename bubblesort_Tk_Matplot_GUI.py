from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
    
##### IMPLEMENTACAO BASICA DO BUBBLE SORT #####
def BubbleSort(lista):
  #Variaveis auxiliares
  aux=0
  troca=True
  x=0
  
  #adicionamos um tamanho para diminuir
  tamanho=len(lista)-1
  
  while troca==True:
    troca=False
    #Utilizarei um for para percorrer a lista
    for x in range (tamanho):
      #Depois vamos fazer as comparaçoes dois a dois
      if lista[x] > lista[x+1]:
        lista[x+1],lista[x]=lista[x],lista[x+1]
        troca=troca+1
        troca=True
    #Podemos otimizar o algoritmo diminuindo o numero de comparaçoes a cada iteracao do for
    tamanho=tamanho-1
    

def testBubble():
  #Testando funcionalidade do bubblesort
  teste = np.array([4,5,10,20])

  for x in range(len(teste)):
    
    lista = np.random.randint(30,size=(teste[x]))
    
    print("Lista ANTES da ordenacao.",teste[x],"Elementos:")
    print(lista)
    
    BubbleSort(lista)
    
    print("Lista DEPOIS da ordenacao.",teste[x],"Elementos:")
    print(lista)
    print("============================================================")
    
##### FRONTEND - TKINTER #####

janela = Tk()
janela.title("Bubble Sort")
janela.geometry("400x300")
janela.resizable(width=False, height=False)

titulo = Label(janela,text="Bubble Sort:",font='Helvetica 15 bold')
titulo.place(x=130, y=3)

texto_inicial = Label(janela,text="Escolha o tipo de ordenacao que vc quer:")
texto_inicial.place(x=75, y=35)

botaoTest=Button(janela,text="Teste aqui",command=testBubble)
botaoTest.place(x=150, y=65)

janela.mainloop()
  
  