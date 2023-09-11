grammar AssignmentSt;
ass:   ID ':=' expr EOF;

expr:	expr '+' term
    |	expr '-' term
    |	term
    ;

term:	term '*' factor
    |	term '/' factor
    |	factor
    ;

factor:
    '(' expr ')'
    | Id
    | Number
    | String
    ;

Number:
   FLOAT | INT;


/* Lexical Rules */
fragment 
        DIGIT: [0-9];
fragment 
        LETTER: [a-zA-Z];
fragment
        ESC : '\\"' | '\\\\' ;

INT     : DIGIT+;

FLOAT   :
        DIGIT+DIGIT*
        | '.' DIGIT+
        ;

String  :
        '"' (ESC|.)*?;

ID      : LETTER(LETTER|DIGIT)*;
WS      : [ \t\n\r]+ -> skip;
