from multiprocessing.sharedctypes import Value
from typing import Counter
from unittest import result
from common import calcula_frequencia, quebra_texto, descobre_tamanho_chave, frequencia_char
from collections import defaultdict

filename="portugues.txt"
lista_frequencia_por_chave = defaultdict()
lista_substrings_por_tamanho_chave = defaultdict()
ic_ingles = 0.0667
ic_portugues = 	0.0745
lingua = "portugues"
ic = 0
tamanho_loop = 0

def descobre_distancia (lingua, char_maior_frequencia): #retorna a chave cifrada
    # o que tiver maior frequencia é o de maior frequencia na lingua
    # do cacartere ate o E, distancia é o caractere da senha   
    char_lingua = ""
    if(lingua == "ingles"):
        char_lingua = "e"
    else: #é portugues
        char_lingua = input("Utilizar A ou E para decifragem: ") #pergunta se quer coloca E ou A
        #char_lingua = "e" or "a"
    
    distancia = (ord(char_maior_frequencia) - ord(char_lingua)) % 26

    resultado = chr(ord("a") + distancia)
    #print("resulado descobre_distancia: ",resultado)
    return resultado

def calcula_valor_letra(letra_cifrada, letra_chave): #decifra a letra
    return ((ord(letra_cifrada) - ord(letra_chave) + 26) % 26) + ord("a")
  
def decifra(texto_original, chave):

    print("chave decifra", chave)
    print(len(chave))
    cont = 0
    resultado = ""
    for letra in texto_original:
        resultado += chr(calcula_valor_letra(letra, chave[cont]))
        cont = cont + 1
        if(cont == len(chave)):
            cont = 0

    f = open("decifrado.txt", "a")
    f.write(resultado)
    f.close()


with open(filename) as file: 
    if(lingua == "ingles"):
        tamanho_loop = 10
        ic = ic_ingles
    else:
        tamanho_loop = 10
        ic=ic_portugues

    texto = file.read()
    for i in range(1,tamanho_loop):
        lista_frequencia_por_chave[i] = list()
        lista_substrings_por_tamanho_chave[i] = list()
        
        texto_separado = quebra_texto(i,texto)
        #print(texto_separado[7])
        for j in range(len(texto_separado)):
            lista_frequencia_por_chave[i].append(calcula_frequencia(texto_separado[j])) 

    tam_chave = descobre_tamanho_chave(lista_frequencia_por_chave,ic, tamanho_loop)
    lista_substrings = quebra_texto(tam_chave,texto) #adiciona na lista todas as substrings do tam chave correspondente
    #print("lista substrings: ",lista_substrings)

    resultado = list()

    #descobrir frequencia dos caracteres de cada substring da lista
    for texto1 in lista_substrings:
        resultado.append(dict(Counter(texto1).most_common(1)))
    
    chave = ""
    for letra in resultado:
        chave = chave + descobre_distancia(lingua, list(letra.keys())[0]) #retorna a chave cifrada
    
    print(chave)
    decifra(texto,chave)

    print("Abra o arquivo Decifrado para encontrar a resposta! =3")

