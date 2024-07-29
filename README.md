# Simplificação e Normalização de Gramáticas Livres de Contexto

Este projeto contém uma implementação em Python para simplificação e normalização de gramáticas livres de contexto (CFGs). O código inclui a identificação de símbolos inúteis e produções vazias.

## Funcionalidades

- **Simplificação da Gramática**: Remove símbolos inúteis, inacessíveis e produções vazias.
- **Saída em JSON**: A gramática simplificada é exportada no formato JSON.

## Formato de Entrada

A gramática deve ser fornecida no formato de um dicionário Python onde as chaves são os símbolos não-terminais e os valores são listas de produções. Exemplo:

```json
{
    'S': ['aAa', 'bBv'],
    'A': ['a', 'aA']
}
