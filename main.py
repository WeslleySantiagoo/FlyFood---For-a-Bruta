def ler_matriz_entrada(l):
    matriz = [input().split() for i in range(l)]
    return matriz

def enderecar_pontos(matriz):
    lista_pontos = []
    coordenadas = {}
    for l in range(len(matriz)):
        linha = matriz[l]
        for c in range(len(linha)):
            coluna = linha[c]
            if coluna != '0' and coluna != 0:
                lista_pontos.append(coluna)
                coordenadas[coluna] = (l, c)
    return r_inicio(lista_pontos), coordenadas

def permutar(lista, inicio=0):
    lista = lista[inicio:]
    if len(lista) <= 1:
        return [lista]
    
    resultado = []
    for i in range(len(lista)):
        elemento_fixo = lista[i]
        resto = lista[:i] + lista[i+1:]
        for p in permutar(resto):
            resultado.append([elemento_fixo] + p)
    return resultado

def arrumar_perm(lista):
    for perm in lista:
        perm.insert(0, 'R')
        perm.append('R')
    return lista

def r_inicio(lista):
    inicio = [item for item in lista if item[0] == 'R']
    resto = [item for item in lista if item[0] != 'R']
    return inicio + resto

def modulo(n):
    if n >= 0:
        return n
    else: return n*(-1)

def distancia_pontos(tupla1, tupla2):
    return modulo(tupla1[0]-tupla2[0]) + modulo(tupla1[1]-tupla2[1])

def calcular_caminhos(lista, coordenadas):
    menor_rota, menor_caminho = [] ,float('inf')
    maior_rota,maior_caminho = [], 0
    for index, perm in enumerate(lista):
        distancia = 0
        for i in range(len(perm)-1):
            ponto1 = perm[i]
            ponto2 = perm[i+1]
            distancia += distancia_pontos(coordenadas[ponto1], coordenadas[ponto2])
        if distancia <= menor_caminho:
            menor_caminho = distancia
            menor_rota = perm
        if distancia >= maior_caminho:
            maior_caminho = distancia
            maior_rota = perm
        print(f'Rota: {' -> '.join(perm)}, Custo: {distancia}')
    return (maior_caminho, maior_rota), (menor_caminho, menor_rota)


def principal():
    # linhas = int((input())[0])
    # matriz = ler_matriz_entrada(linhas)
    matriz = [
        ['0', 'A', '0', '0', '0'],
        ['0', '0', '0', 'C', '0'],
        ['0', 'B', '0', '0', '0'],
        ['R', '0', '0', '0', 'D'],
        ['0', '0', '0', '0', '0']
    ]
    lista_de_pontos, coordenadas = enderecar_pontos(matriz)
    permutacoes = arrumar_perm(permutar(lista_de_pontos, 1))
    maior_rota, menor_rota = calcular_caminhos(permutacoes, coordenadas)
    print(f"Rota: {' -> '.join(maior_rota[1][1:-1])} Total: {maior_rota[0]}")
    print(f"Rota: {' -> '.join(menor_rota[1][1:-1])} Total: {menor_rota[0]}")

if __name__ == "__main__":
    principal()

