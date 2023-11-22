% Facts
parent(m, p).
parent(m, x).
parent(f, p).
parent(f, x).

male(m).
female(f).

% Rules
mother(M, P) :- parent(M, P), female(M).
father(F, P) :- parent(F, P), male(F).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
grandparent(G, P) :- parent(G, X), parent(X, P).
uncle(U, N) :- sibling(U, P), parent(P, N), male(U).
aunt(A, N) :- sibling(A, P), parent(P, N), female(A).
sister(S, X) :- sibling(S, X), female(S).
brother(B, X) :- sibling(B, X), male(B).
