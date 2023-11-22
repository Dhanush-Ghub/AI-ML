% Substring Predicate
substring(S, Start, Length, Sub) :-
    sub_string(S, Start, Length, _, Sub).

% String Position Predicate
string_position(String, Substring, Position) :-
    sub_string(String, Position, _, _, Substring).

% Palindrome Predicate
palindrome(S) :-
    reverse(S, S).