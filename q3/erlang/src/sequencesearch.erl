% This is the main module responsible for searching the target sumup in a given list
-module(sequencesearch).
-import(io,[fwrite/1]).
% Export the sequence search, which takes as parameters the list and the target
-export([sequencesearch/2, sumtotarget/2, start/0]).


% Sum up the elements until the target is achieved or exceeded
sumtotarget([]) -> 0
sumtotarget([_|T], Target) -> 
    sumtotarget()


sequencesearch([H|T], Target) ->
   fwrite("Sequence Search ~f\n", Target).
   sumtotarget(T, Target)

start()->
    X = [1,2,3,4,5,6,7,8],
    Target =  10
    sequencesearch(X, T)