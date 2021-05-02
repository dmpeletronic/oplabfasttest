### 4.

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
| `179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368` | `1025` |

#### 4.1 Solution proposal

Beside the fact we are dealing with bignumbers, the algorithm is:
while N > 1:
   if is even: divide N/2
   else
       find the closest power of 2
       if bigger than N
          sum 1
       else 
          sub 1
Count every operation 



#### 4.2 Solution compile, test and run

The solution is proposed in python. In python, we are using the native implementation of bignumbers, so we don't need to deal with it. 

Run:
    python3 cli/cli.py
  
Run unit test cases from base folder:
    python3 -m unittest tests.test

#### 4.3 Discussions

To know if a number is a power of 2, we just need to count the number of ones. 
Exemples: 
    40 is not power of 2: 0x28 = 0x101000, there are 2 ones
    32 is power of 2: 0x20 = 0x100000, thre is only 1 one

There are optimun ways to find the closest power of 2:
Suppose the number 40, 0x28, 0x101000.
For the lower power of 2, rotate to right and clear all 1 except the most left.
Example:
40 = 0x28 =0b00101000
                |_________rotate this number 1 to the right and count
            0b00000001
                    |____rotate the 1 to the left the "count" times from step before
            0b00100000
                |_________this is the lower power of 2: 0x20 = 32decimal

For the higher power of 2, duplicate the number, rotate to right and clear all 1 than rotate back
Example:
40 = 0x28 =0b00101000
                << 1    duplicate
            0b01010000
                |__________rotate this number 1 to the right and count
            0b00000001
                    |____rotate the 1 to the left the "count" times from step before
            0b00100000
                |_________this is the lower power of 2: 0x40 = 64decimal    

Regarding the BigNumber operations native in Python, I could reimplement the wheel but it would take some time to develop and unittest it. I assumed that the knowledge of bignumber algorithms to sum, subtract, divide, rotate, bitwise, and others, wasn't the focus of this test. 