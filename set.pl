% Union Predicate
union(Set1, Set2, Union) :-
    union(Set1, Set2, Union).

% Intersection Predicate
intersection(Set1, Set2, Intersection) :-
    intersection(Set1, Set2, Intersection).

% Complement Predicate
complement(UniversalSet, Set, Complement) :-
    subtract(UniversalSet, Set, Complement).
