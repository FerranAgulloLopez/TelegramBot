# Generated from Enquestes.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("g\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\6\2\35\n\2\r\2\16\2\36\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\6\4/\n\4\r\4\16\4\60\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\6\6@\n")
        buf.write("\6\r\6\16\6A\3\6\3\6\3\7\3\7\3\7\3\7\6\7J\n\7\r\7\16\7")
        buf.write("K\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7\tY\n\t")
        buf.write("\f\t\16\t\\\13\t\3\n\3\n\3\13\3\13\3\f\6\fc\n\f\r\f\16")
        buf.write("\fd\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\2\2d\2\34\3")
        buf.write("\2\2\2\4$\3\2\2\2\6*\3\2\2\2\b\62\3\2\2\2\n9\3\2\2\2\f")
        buf.write("E\3\2\2\2\16M\3\2\2\2\20R\3\2\2\2\22]\3\2\2\2\24_\3\2")
        buf.write("\2\2\26b\3\2\2\2\30\35\5\4\3\2\31\35\5\6\4\2\32\35\5\b")
        buf.write("\5\2\33\35\5\n\6\2\34\30\3\2\2\2\34\31\3\2\2\2\34\32\3")
        buf.write("\2\2\2\34\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37")
        buf.write("\3\2\2\2\37 \3\2\2\2 !\5\f\7\2!\"\7\3\2\2\"#\7\2\2\3#")
        buf.write("\3\3\2\2\2$%\5\24\13\2%&\7\4\2\2&\'\7\5\2\2\'(\5\26\f")
        buf.write("\2()\7\6\2\2)\5\3\2\2\2*+\5\24\13\2+,\7\4\2\2,.\7\7\2")
        buf.write("\2-/\5\16\b\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61")
        buf.write("\3\2\2\2\61\7\3\2\2\2\62\63\5\24\13\2\63\64\7\4\2\2\64")
        buf.write("\65\7\b\2\2\65\66\5\24\13\2\66\67\7\t\2\2\678\5\24\13")
        buf.write("\28\t\3\2\2\29:\5\24\13\2:;\7\4\2\2;<\7\n\2\2<=\5\24\13")
        buf.write("\2=?\7\13\2\2>@\5\20\t\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2")
        buf.write("AB\3\2\2\2BC\3\2\2\2CD\7\f\2\2D\13\3\2\2\2EF\7\23\2\2")
        buf.write("FG\7\4\2\2GI\7\r\2\2HJ\5\24\13\2IH\3\2\2\2JK\3\2\2\2K")
        buf.write("I\3\2\2\2KL\3\2\2\2L\r\3\2\2\2MN\5\22\n\2NO\7\4\2\2OP")
        buf.write("\5\26\f\2PQ\7\16\2\2Q\17\3\2\2\2RS\7\17\2\2ST\5\22\n\2")
        buf.write("TU\7\20\2\2UV\5\24\13\2VZ\7\21\2\2WY\7\20\2\2XW\3\2\2")
        buf.write("\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\21\3\2\2\2\\Z\3\2\2")
        buf.write("\2]^\7\24\2\2^\23\3\2\2\2_`\7\22\2\2`\25\3\2\2\2ac\7\23")
        buf.write("\2\2ba\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2e\27\3\2\2")
        buf.write("\2\t\34\36\60AKZd")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'END'", "':'", "'PREGUNTA'", "'?'", "'RESPOSTA'", 
                     "'ITEM'", "'->'", "'ALTERNATIVA'", "'['", "']'", "'ENQUESTA'", 
                     "';'", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "WORD", "DIGIT", "SL", "LINE_COMMENT" ]

    RULE_root = 0
    RULE_pregunta = 1
    RULE_resposta = 2
    RULE_item = 3
    RULE_alternativa = 4
    RULE_definicioEnquesta = 5
    RULE_opcioResposta = 6
    RULE_opcioAlternativa = 7
    RULE_identifierOpcio = 8
    RULE_identifier = 9
    RULE_text = 10

    ruleNames =  [ "root", "pregunta", "resposta", "item", "alternativa", 
                   "definicioEnquesta", "opcioResposta", "opcioAlternativa", 
                   "identifierOpcio", "identifier", "text" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    ID=16
    WORD=17
    DIGIT=18
    SL=19
    LINE_COMMENT=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definicioEnquesta(self):
            return self.getTypedRuleContext(EnquestesParser.DefinicioEnquestaContext,0)


        def EOF(self):
            return self.getToken(EnquestesParser.EOF, 0)

        def pregunta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.PreguntaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.PreguntaContext,i)


        def resposta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.RespostaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.RespostaContext,i)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ItemContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ItemContext,i)


        def alternativa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.AlternativaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.AlternativaContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = EnquestesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 22
                    self.pregunta()
                    pass

                elif la_ == 2:
                    self.state = 23
                    self.resposta()
                    pass

                elif la_ == 3:
                    self.state = 24
                    self.item()
                    pass

                elif la_ == 4:
                    self.state = 25
                    self.alternativa()
                    pass


                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.ID):
                    break

            self.state = 30
            self.definicioEnquesta()
            self.state = 31
            self.match(EnquestesParser.T__0)
            self.state = 32
            self.match(EnquestesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PreguntaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def text(self):
            return self.getTypedRuleContext(EnquestesParser.TextContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_pregunta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPregunta" ):
                return visitor.visitPregunta(self)
            else:
                return visitor.visitChildren(self)




    def pregunta(self):

        localctx = EnquestesParser.PreguntaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pregunta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.identifier()
            self.state = 35
            self.match(EnquestesParser.T__1)
            self.state = 36
            self.match(EnquestesParser.T__2)
            self.state = 37
            self.text()
            self.state = 38
            self.match(EnquestesParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RespostaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def opcioResposta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.OpcioRespostaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.OpcioRespostaContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_resposta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResposta" ):
                return visitor.visitResposta(self)
            else:
                return visitor.visitChildren(self)




    def resposta(self):

        localctx = EnquestesParser.RespostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_resposta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.identifier()
            self.state = 41
            self.match(EnquestesParser.T__1)
            self.state = 42
            self.match(EnquestesParser.T__4)
            self.state = 44 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 43
                self.opcioResposta()
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.DIGIT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.IdentifierContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.identifier()
            self.state = 49
            self.match(EnquestesParser.T__1)
            self.state = 50
            self.match(EnquestesParser.T__5)
            self.state = 51
            self.identifier()
            self.state = 52
            self.match(EnquestesParser.T__6)
            self.state = 53
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlternativaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.IdentifierContext,i)


        def opcioAlternativa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.OpcioAlternativaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.OpcioAlternativaContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_alternativa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternativa" ):
                return visitor.visitAlternativa(self)
            else:
                return visitor.visitChildren(self)




    def alternativa(self):

        localctx = EnquestesParser.AlternativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_alternativa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.identifier()
            self.state = 56
            self.match(EnquestesParser.T__1)
            self.state = 57
            self.match(EnquestesParser.T__7)
            self.state = 58
            self.identifier()
            self.state = 59
            self.match(EnquestesParser.T__8)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.opcioAlternativa()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.T__12):
                    break

            self.state = 65
            self.match(EnquestesParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefinicioEnquestaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(EnquestesParser.WORD, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.IdentifierContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_definicioEnquesta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicioEnquesta" ):
                return visitor.visitDefinicioEnquesta(self)
            else:
                return visitor.visitChildren(self)




    def definicioEnquesta(self):

        localctx = EnquestesParser.DefinicioEnquestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_definicioEnquesta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(EnquestesParser.WORD)
            self.state = 68
            self.match(EnquestesParser.T__1)
            self.state = 69
            self.match(EnquestesParser.T__10)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.identifier()
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpcioRespostaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierOpcio(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierOpcioContext,0)


        def text(self):
            return self.getTypedRuleContext(EnquestesParser.TextContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_opcioResposta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcioResposta" ):
                return visitor.visitOpcioResposta(self)
            else:
                return visitor.visitChildren(self)




    def opcioResposta(self):

        localctx = EnquestesParser.OpcioRespostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_opcioResposta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.identifierOpcio()
            self.state = 76
            self.match(EnquestesParser.T__1)
            self.state = 77
            self.text()
            self.state = 78
            self.match(EnquestesParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpcioAlternativaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierOpcio(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierOpcioContext,0)


        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_opcioAlternativa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcioAlternativa" ):
                return visitor.visitOpcioAlternativa(self)
            else:
                return visitor.visitChildren(self)




    def opcioAlternativa(self):

        localctx = EnquestesParser.OpcioAlternativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opcioAlternativa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(EnquestesParser.T__12)
            self.state = 81
            self.identifierOpcio()
            self.state = 82
            self.match(EnquestesParser.T__13)
            self.state = 83
            self.identifier()
            self.state = 84
            self.match(EnquestesParser.T__14)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.T__13:
                self.state = 85
                self.match(EnquestesParser.T__13)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierOpcioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(EnquestesParser.DIGIT, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_identifierOpcio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierOpcio" ):
                return visitor.visitIdentifierOpcio(self)
            else:
                return visitor.visitChildren(self)




    def identifierOpcio(self):

        localctx = EnquestesParser.IdentifierOpcioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifierOpcio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(EnquestesParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = EnquestesParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(EnquestesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.WORD)
            else:
                return self.getToken(EnquestesParser.WORD, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_text

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = EnquestesParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 95
                self.match(EnquestesParser.WORD)
                self.state = 98 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.WORD):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





