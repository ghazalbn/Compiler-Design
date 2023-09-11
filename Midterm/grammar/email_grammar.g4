grammar email_grammar;

compilationUnit: EMAIL EOF;

EMAIL:
    Loc ('.' Loc)* '@' Dom ('.' Dom)+;

fragment Loc :
    [a-zA-Z0-9!$&()*+,;=:_~-]+;

fragment Dom :
    [a-zA-Z0-9-]+;
