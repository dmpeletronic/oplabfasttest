### 1.
Escreva uma função `f(area)` que tem como entrada a área total de um **quadrilátero** (entre 1 e 1000000, inclusive), e retorne um _array_ de áreas dos maiores **quadrados** que você poderia colocar dentro do quadrilátero, começando pelo maior quadrado.
Por exemplo: `f(12)` deve retornar `[9, 1, 1, 1]`.

|Entrada|Saída|
|--|--|
| `15324` | `[15129,169,25,1]` |
| `12` | `[9, 1, 1, 1]` |

### 2.
Define-se `p` como sendo um número de infinitos dígitos composto pela concatenação de todos os números primos (`2357111317192329...`).
Escreva uma função `f(n)`que tem como entrada um número inteiro `n` que representa um índice (entre 0 e 10000) e retorne um número com os 5 próximos dígitos de `p`, a partir do índice `n`.
Por exemplo: `f(3)` deve retornar `71113`.

|Entrada|Saída|
|--|--|
| `0` | `23571` |
| `3` | `71113` |

### 3.
Dada uma lista de inteiros positivos `l` e um inteiro positivo alvo `t`, escreva uma função `f(l, t)` que verifica se há pelo menos uma sequencia de inteiros positivos dentro da lista que podem ser somados e têm como resultado `t`, e retorna a menor lista contendo os menores índices de início e fim onde essa sequência pode ser encontrada, ou retorna o _array_ `[-1, 1]` caso não encontre.
Por exemplo, dado a lista `l = [4, 3, 5, 7, 8]` e `t = 12`; `f(l, t)` deve retornar a lista `[0, 2]`, já que `4 + 3 + 5 = 12`, mesmo havendo uma menor sequência que aparece depois na lista (`5 + 7`). Por outro lado, dado uma lista `l = [1, 2, 3, 4]` e `t = 15`, o retorno de `f(l, t)` deve ser `[-1, 1]`.

Algumas condições para o problema:
- Cada lista `l` contém pelo menos 1 elemento, porém não mais do que 100.
- Cada elemento de `l` está entre 1 e 100.
- `t` é um inteiro positivo que não excede 250.
- O primeiro elemento da lista `l` tem índice 0.
- A lista retornada por `f(l, t)` deve ter o índice de início igual ou menor que o índice do final.

|Entrada|Saída|
|--|--|
| `[1, 2, 3, 4], 15` | `[-1, -1]` |
| `[4, 3, 10, 2, 8], 12` | `[2, 3]` |

## 4.

Escreva uma função `f(n)` que aceita um inteiro positivo `n` (com até 309 dígitos) e retorno o número mínimo de operações necessárias para transformar esse número no número 1.

As operações são as seguintes:

- Adiciona 1
- Subtrai 1
- Divide por 2 (apenas quando o número a ser dividido é par)

Por examplo:
`f(4)` retorna 2, porque 4 -> 2 -> 1
`f(15)` retorna 5, porque 15 -> 16 -> 8 -> 4 -> 2 -> 1

|Entrada|Saída|
|--|--|
| `15` | `5` |
| `4` | `2` |
| `1248390` | `27`|
| `179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368` | 1025 |