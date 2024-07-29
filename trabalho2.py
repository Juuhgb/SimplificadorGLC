import json

def ler_gramatica(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)

def escrever_gramatica(nome_arquivo, gramatica):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(gramatica, arquivo, indent=4)

def remover_simbolos_inalcancaveis(gramatica):
    alcançados = set()
    para_visitar = {'S'}
    
    while para_visitar:
        atual = para_visitar.pop()
        if atual in gramatica:
            alcançados.add(atual)
            for producao in gramatica[atual]:
                for simbolo in producao:
                    if simbolo.isupper() and simbolo not in alcançados:
                        para_visitar.add(simbolo)
    
    return {não_terminal: producoes for não_terminal, producoes in gramatica.items() if não_terminal in alcançados}

def remover_producoes_vazias(gramatica):
    nulos = set()
    for não_terminal in gramatica:
        if "" in gramatica[não_terminal]:
            nulos.add(não_terminal)
    
    mudanças = True
    while mudanças:
        mudanças = False
        novas_producoes = {}
        for não_terminal, producoes in gramatica.items():
            novas_producoes_para_nt = []
            for producao in producoes:
                if any(simbolo in nulos for simbolo in producao):
                    novas_producoes_para_nt.extend(gerar_producoes(producao, nulos))
                else:
                    novas_producoes_para_nt.append(producao)
            novas_producoes[não_terminal] = list(set(novas_producoes_para_nt))
        if novas_producoes != gramatica:
            mudanças = True
            gramatica = novas_producoes
    
    gramatica = {nt: [prod for prod in prods if prod != ""] for nt, prods in gramatica.items()}
    return gramatica

def gerar_producoes(producao, nulos):
    producoes = [producao]
    for i in range(len(producao)):
        if producao[i] in nulos:
            novas_prods = [prod[:i] + prod[i+1:] for prod in producoes]
            producoes.extend(novas_prods)
    return list(set(producoes))

def remover_producoes_unitarias(gramatica):
    mudanças = True
    while mudanças:
        mudanças = False
        novas_producoes = {}
        for nt, producoes in gramatica.items():
            novas_producoes_para_nt = []
            for producao in producoes:
                if len(producao) == 1 and producao.isupper():
                    mudanças = True
                    novas_producoes_para_nt.extend(gramatica[producao])
                else:
                    novas_producoes_para_nt.append(producao)
            novas_producoes[nt] = list(set(novas_producoes_para_nt))
        if novas_producoes != gramatica:
            gramatica = novas_producoes
    
    return gramatica

def principal():
    gramatica = ler_gramatica('E:/VsCode/Python/TeoriaDaComputacao/2trabalho/entrada.json')
    
    gramatica = remover_simbolos_inalcancaveis(gramatica)
    gramatica = remover_producoes_vazias(gramatica)
    gramatica = remover_producoes_unitarias(gramatica)
    
    escrever_gramatica('saida.json', gramatica)

if __name__ == '__main__':
    principal()