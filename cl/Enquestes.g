grammar Enquestes;

root: (pregunta | resposta | item | alternativa)+ definicioEnquesta 'END' EOF;

pregunta: identifier ':' 'PREGUNTA' text '?';
resposta: identifier ':' 'RESPOSTA' opcioResposta+;
item: identifier ':' 'ITEM' identifier '->' identifier;
alternativa: identifier ':' 'ALTERNATIVA' identifier '[' opcioAlternativa+ ']';
definicioEnquesta: 'E' ':' 'ENQUESTA' identifier+;


opcioResposta: identifierOpcio ':' text ';';
opcioAlternativa: '(' identifierOpcio ',' identifier ')' (',')*;
identifierOpcio: DIGIT;
identifier : ID;
text: WORD+;


ID: [a-zA-Z]DIGIT+;
WORD: [a-zA-Z][a-zA-Z0-9\u0080-\u00FF]*;
DIGIT: [0-9];
SL: [ \n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;