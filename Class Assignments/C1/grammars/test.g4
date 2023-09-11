/*
grammar test
Grammar of simple mathematical expressions. Without any attribute and action.
Test grammar for demo and education porpuse.
- Example of input which accepts by the grammar:
-- x = a + b * c

Written by: Morteza Zakeri
*/

grammar test;
start:
    Id '=' expr EOF
    ;

expr:
    expr '+' term #rule_plus
    | expr '-' term  #rule_minus
    | term #rule3
    ;

term:
    term '*' fact
    | term '/' fact
    | fact
    ;

fact:
    Id
    | Number
    | '('expr')'
    | EOF
    ;

/* Lexical rules*/
Plus: '+';
MINUS: '-';
MUL: '*';
DIVIDE: '/';
ASSIGN: '=';


Id: IDENTIFIER;
Number: NUMBER;

fragment IDENTIFIER: ([a-zA-Z] | Special)+;
fragment NUMBER: [0-9]+;
Special: '?'|'&'|'^'|'%'|'$'|'#'|'@';

Newline: '\n' -> skip;
Whitespace: [ \t\r]+ -> channel(HIDDEN);

Comment
   : '/*' .*? '*/' -> channel(HIDDEN)
   ;

LineComment
   : '//' ~ [\r\n]* -> channel(HIDDEN)
   ;

