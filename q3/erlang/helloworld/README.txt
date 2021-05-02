Need to compile inside the interpreter.
Need to call the helloworld function inside the interpreter.
The "." is extremly important.

root@129845161d3d:/opt/oplab/q3/erlang/helloworld# erl hello.erl 
Erlang/OTP 22 [erts-10.6.4] [source] [64-bit] [smp:8:8] [ds:8:8:10] [async-threads:1]

Eshell V10.6.4  (abort with ^G)
1> c(hello).
{ok,hello}
2> hello:helloworld().
Hello, Erlang World!
ok