grammar Enquestes;

root: enquesta EOF;
enquesta: (pregunta | resposta | item | alternativa)+ definicioEnquesta 'END';

pregunta: identifier ':' 'PREGUNTA' text '?';
resposta: identifier ':' 'RESPOSTA' (opcioResposta)+;
item: identifier ':' 'ITEM' identifier '->' identifier;
alternativa: identifier ':' 'ALTERNATIVA' identifier '[' opcioAlternativa+ ']';
definicioEnquesta: 'E' ':' 'ENQUESTA' (identifier)+;


opcioResposta: idopcio ':' text ';';
opcioAlternativa: '(' idopcio ',' identifier ')' (',')*;
idopcio: DIGIT;
identifier : ID+;
text: WORD+;


ID: [a-zA-Z]DIGIT+;
WORD: [a-zA-Z][a-zA-Z0-9\u0080-\u00FF]*;
WS: [ \n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
DIGIT: [0-9];
