grammar Cow;

compilationUnit
    : Instruction* EOF
    ;

Instruction
    : 'moo'
    | 'moO'
    | 'mOo'
    | 'mOO'
    | 'Moo'
    | 'MoO'
    | 'MOo'
    | 'MOO'
    | 'OOO'
    | 'MMM'
    | 'OOM'
    | 'oom'
    ;

Newline: '\n' -> skip;
Whitespace: [ \t\r]+ -> channel(HIDDEN);