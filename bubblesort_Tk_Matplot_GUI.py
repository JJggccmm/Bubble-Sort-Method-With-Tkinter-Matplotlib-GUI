from cProfile import label
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter
    
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
    
###### TESTE DO ALGORITMO ########
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
       
        
##### UTILIZANDO NUMEROS ALEATORIOS NO BUBBLE SORT
def ordenacaoAleatoria():
  
    texto1="Numeros Aleatorios"
    
    testes=np.array([500,1000,1500,2000,2500,4000,5500,7500])
    #Tambem irei criar um array para armazenar o resultado em segundos de cada teste
    resultados=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    labels=np.array([])
    aux=100

    #Com esse for conseguiremos testar nosso BubbleSort com os valores de 1k ate 15k de elementos
    for x in range (len(testes)):
        #Primeiro iremos iniciar um vetor do tamanho da vez(indicado por testes[x])
        lista = np.random.randint(2500,size=(testes[x]))

        #Temporizador 
        inicio = perf_counter()
        BubbleSort(lista)
        fim = perf_counter()

        resultados[x]=fim-inicio
        #O tempo sera armazenado em vetor na mesma posicao do teste que esta sendo feito
        resultados[x]=round(resultados[x],3)
        
        print("Para ",testes[x]," elementos foi gasto",resultados[x],"segundos")
        
        aux=aux+20
        label=Label(janela,text=("Para ",testes[x]," elementos foi gasto",resultados[x],"segundos"))
        label.place(x=60, y=aux)
        janela.update

    plotaGrafico(testes,resultados,texto1)
    
########## PIOR CASO ##########
def piorCaso():
  
  texto2="Pior Caso"
      
  #O código sera bem parecido
  testes=np.array([500,1000,1500,2000,2500,4000,5500,7500])
  resultados2=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
  labels=np.array([])
  aux=100

  for x in range (len(testes)):
    #Só que aqui iremos gerar uma lista ordenada e depois invertela
    lista = np.arange(testes[x])
    listaInversa = lista[::-1]

    
    inicio = perf_counter()
    BubbleSort(listaInversa)
    fim = perf_counter()

    resultados2[x]=fim-inicio
    resultados2[x]=round(resultados2[x],2)

    print("Para ",testes[x]," elementos foi gasto",resultados2[x],"segundos")  
    aux=aux+20
    label=Label(janela,text=("Para ",testes[x]," elementos foi gasto",resultados2[x],"segundos"))
    label.place(x=60, y=aux)
    janela.update  
    
  plotaGrafico(testes,resultados2,texto2)
    
  
####### Plotando grafico com tkinter ########   
def plotaGrafico(testes,resultados,texto):
  plt.title("Counting Sort")
  plt.plot(testes,resultados, label=texto,marker='o')
  plt.ylabel('Tempo(s)')
  plt.xlabel('Nº de Elementos')
  plt.legend()
  plt.show()
    
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
botaoTest.place(x=300, y=3)

botao1 = Button(janela,text="Numeros Aleatorios",command=ordenacaoAleatoria)
botao1.place(x=50, y=65)

botao2 = Button(janela,text="Pior Caso",command=piorCaso)
botao2.place(x=250, y=65)

janela.mainloop()
  
  