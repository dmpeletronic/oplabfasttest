### 1.
Escreva uma função `f(area)` que tem como entrada a área total de um **quadrilátero** (entre 1 e 1000000, inclusive), e retorne um _array_ de áreas dos maiores **quadrados** que você poderia colocar dentro do quadrilátero, começando pelo maior quadrado.
Por exemplo: `f(12)` deve retornar `[9, 1, 1, 1]`.

|Entrada|Saída|
|--|--|
| `15324` | `[15129,169,25,1]` |
| `12` | `[9, 1, 1, 1]` |


#### 1.1 Solution proposal

After analyzing and understanding the problem, the proposed solution algorithm is:

While(remaing_area > 0)
    1. Find the squareroot of remaining area
    2. Floor the result
    3. Add the result to list
        3.1 only if the remaining are is perfectly divided by the size of the square
    4. Get the diffrence from remaing area and the result
    4. Update the remaing area with the diference


#### 1.2 Solution compile, test and run

The solution was implemented in C/C++. It is C style using some features from C++.
To run the development environment please check the docker-env folder.

Compile:
 - Access the /opt/oplab/q1 folder, and execute:
 ```mkdir build
    cd build
    cmake ../
    make
 ```

Run cli:
```Usage: ./cli TotalArea
   ./cli 12
   ./cli 15324
```

Run test cases:
 ```./unittest```


#### 1.3 Discussions

There is a missunderstanding in the question enunciate, due to the following example:

Total area: 15324
First square: 123x123 => 15129
Second square: 13x13 => 169
It means that if we use the first square, it won't be possible to have an square of size 13x13 (169), because if we add this case, the total area won't fit the informed area of 15324. 

See the example below:
<rawtext>

        123                      13
     _______________________ _____________
    |                       |             | 
    |                       |             |
    |                       |  169 area   |13
    |                       |             |
123 |       15129 area      |_____________|
    |                       |      |
    |                       |25area|
    |                       |______|
    |_______________________|_|1 area 
</rawtext>

To became a real quadrilateral, we should have 4 edges and 4 angles, but as you can see, there is more than that. If we sumup the 4 squares areas, we will achieve the 15324, but this is not the enunciate request.

The ideal solution in my view, would be to find the biggest square where the quadrilateral still will have 4 egdes and 4 angles.

