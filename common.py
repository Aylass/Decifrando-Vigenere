from string import ascii_lowercase
from collections import defaultdict
from typing import Counter


def quebra_texto(tamChave, textoConteudo):
    resultado = list()

    for i in range(0,tamChave):
        resultado.append(textoConteudo[i::tamChave])

    return resultado

def calcula_frequencia(subString):
    tamanho = len(subString)
    resultado = 0

    for letra in ascii_lowercase:
        frequencia = subString.count(letra)
        resultado+= frequencia * (frequencia-1)
    
    resultado = resultado / (tamanho * (tamanho - 1))
    return resultado
    

def descobre_tamanho_chave(lista_frequencia_por_chave, ic, tamanho_loop):
    resultado = tamanho_loop;
    aux = -5;
    tamanhoChave = 0;

    for i in range(1,len(lista_frequencia_por_chave)):
        #print("lista: ", lista_frequencia_por_chave[i])
        aux2 = lista_frequencia_por_chave[i]
        aux = (aux2[0] - ic)
        
        if(aux < 0):
            aux = aux * -1
        #print("aux1: ",aux)

        if aux < resultado:
            resultado = aux
            tamanhoChave = i;
            #print("aux: ",aux)

    #print("IC:",resultado)
    #print("tamanhoChave:",tamanhoChave)
    return tamanhoChave #retorna o provavel tamanho da chave


def frequencia_char(texto, lingua):
    #print("Substring frequencia_char: ", texto)
    #calcula o caractere que tem maior frequencia na substring
    char_maior_frequencia = calcula_char_maior_frequencia(texto)

    distancia = descobre_distancia(lingua, char_maior_frequencia)
    return char_maior_frequencia

def descobre_distancia (lingua, char_maior_frequencia):
    # o que tiver maior frequencia é o de maior frequencia na lingua
    # do cacartere ate o E, distancia é o caractere da senha   
    char_lingua = ""
    if(lingua == "ingles"):
        char_lingua = "e"
    else: #é portugues
        char_lingua = "a"
    
    if(ord(char_lingua) >= ord(char_maior_frequencia)):
        distancia = ord(char_lingua) - ord(char_maior_frequencia)
    else:
        distancia = ord(char_maior_frequencia) - ord("z")
        distancia = distancia + (ord("a") - ord(char_lingua))

    #print("Distancia: ",distancia)
    return distancia


def calcula_char_maior_frequencia(texto):
    from collections import Counter
    counts = Counter(texto)
    #print("max: ", max(counts, key = counts.get))
    #print("\n")
    resposta = max(counts, key = counts.get)
    return resposta

    




    