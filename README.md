# NOTAS-MUSICAIS
Um pequeno sistema desenvolvido em Python para execução no terminal, com o objetivo de ensinar notas musicais por meio de um jogo simples e interativo.

# Código de Cores
O estilo de formatação pode ser feito por:

Estilo de Formatação
| Código | Efeito                  |
| ------ | ----------------------- |
| 0      | Reset (volta ao normal) |
| 1      | Negrito                 |
| 2      | Menos intenso           |
| 4      | Sublinhado              |
| 5      | Piscando                |
| 7      | Inverter cores          |
| 8      | Oculto                  |
| 9      | Tachado                 |


Cores de Texto
| Código | Cor          |
| ------ | ------------ |
| 30     | Preto        |
| 31     | Vermelho     |
| 32     | Verde        |
| 33     | Amarelo      |
| 34     | Azul         |
| 35     | Magenta/Roxo |
| 36     | Ciano        |
| 37     | Branco       |

Cores de Fundo
| Código | Cor          |
| ------ | ------------ |
| 40     | Preto        |
| 41     | Vermelho     |
| 42     | Verde        |
| 43     | Amarelo      |
| 44     | Azul         |
| 45     | Magenta/Roxo |
| 46     | Ciano        |
| 47     | Branco       |

Versões Brilhantes de Texto
| Código | Cor              |
| ------ | ---------------- |
| 90     | Cinza Escuro     |
| 91     | Vermelho Claro   |
| 92     | Verde Claro      |
| 93     | Amarelo Claro    |
| 94     | Azul Claro       |
| 95     | Magenta Claro    |
| 96     | Ciano Claro      |
| 97     | Branco Brilhante |

Fundo Brilhante
| Código | Cor              |
| ------ | ---------------- |
| 100    | Cinza            |
| 101    | Vermelho Claro   |
| 102    | Verde Claro      |
| 103    | Amarelo Claro    |
| 104    | Azul Claro       |
| 105    | Magenta Claro    |
| 106    | Ciano Claro      |
| 107    | Branco Brilhante |

Exemplo em Código:
```
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m'
}
```

Sites:

https://codigopython.blogs.sapo.pt/cores-no-terminal-59499
https://raccoon.ninja/pt/post/dev/tabela-de-cores-ansi-python/