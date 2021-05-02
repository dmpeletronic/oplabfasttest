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


#### 3.1 Solution proposal

Brute force.
Do exactly what the description of the question requests.
Given the starting point index 0, accumulates the value until target is reached or exceeded. If reached, we have our starting and ending index; if exceeded, lets increment the starting point index and repeat. 
If the target is never achieved, return the error code (-1,1).


#### 3.2 Solution compile, test and run

I did not create the cli for this solution because it is not usable to enter with an array of values manually. Please check the unittest.

Run unit test cases from base folder:
    python3 -m unittest tests.test

#### 3.3 Discussions
I tryed with Erlang, but I was taking too much time to understand the details of the language.
As I understood, everything must created as a recursion. For this particular problem, it seems that the tail recursion is something that I could use. But time is up to me here.
Then moved back to python. Python is life!