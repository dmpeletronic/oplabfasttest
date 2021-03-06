### 2.
Define-se `p` como sendo um número de infinitos dígitos composto pela concatenação de todos os números primos (`2357111317192329...`).
Escreva uma função `f(n)`que tem como entrada um número inteiro `n` que representa um índice (entre 0 e 10000) e retorne um número com os 5 próximos dígitos de `p`, a partir do índice `n`.
Por exemplo: `f(3)` deve retornar `71113`.

|Entrada|Saída|
|--|--|
| `0` | `23571` |
| `3` | `71113` |


#### 2.1 Solution proposal

First, it calculates the first 10000 primes and store them into the string that will be checked against the requested position.
The optimizations are discussed in section 2.3.

#### 2.2 Solution compile, test and run

The solution is proposed in Rust. It uses the Cargo builder from Rust.
To run the development environment please check the docker-env folder.

Compile:
 - Access the /opt/oplab/q2/rust/prime_generator folder, and execute:
    cargo build
Run:
    cargo run POSITION
 or 
    ./target/debug/prime_generator POSITION
 where POSITION is the index position N to look for the 5 p digits
 
Run unit test cases:
    cargo test

#### 1.3 Discussions

The initial idea was to separate the prime numbers generation from the search for the requested position into two diffrents applications. This choice was evaluated because finding the Nth prime number can be a time consuming task, even when appling a lot of optimizations as described in this [link](https://levelup.gitconnected.com/how-to-find-the-nth-prime-number-c16dac27963). 
Doing so, we could optimize the search of the required Nth prime number to an ordered lookup table.
But, after doing some tests with Rust, it was detected that it takes less than 200ms to calculate them all. As there is no time restriction for the problem solution, we decided to go with runtime calculation all the 10005 primes.

Some interesting learning about rust:
 - cargo: a build system for rust instead of calling rustc
 - cargo new ProjName: create a new project (create Cargo.toml that defines and configures the project)
 - cargo build: builds the app into target/debug folder
 - cargo run: runs the builded app
 - cargo check: check if code will compile
 - cargo test: compiles and runs unittest and integration tests