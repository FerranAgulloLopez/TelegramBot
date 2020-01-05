# Generated from Enquestes.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("n\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\6\3\"\n\3\r\3\16\3#\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\6\5\63\n\5\r\5")
        buf.write("\16\5\64\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\6\7D\n\7\r\7\16\7E\3\7\3\7\3\b\3\b\3\b\3\b\6\b")
        buf.write("N\n\b\r\b\16\bO\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\7\n]\n\n\f\n\16\n`\13\n\3\13\3\13\3\f\6\fe\n\f")
        buf.write("\r\f\16\ff\3\r\6\rj\n\r\r\r\16\rk\3\r\2\2\16\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\2\2\2k\2\32\3\2\2\2\4!\3\2\2\2\6")
        buf.write("(\3\2\2\2\b.\3\2\2\2\n\66\3\2\2\2\f=\3\2\2\2\16I\3\2\2")
        buf.write("\2\20Q\3\2\2\2\22V\3\2\2\2\24a\3\2\2\2\26d\3\2\2\2\30")
        buf.write("i\3\2\2\2\32\33\5\4\3\2\33\34\7\2\2\3\34\3\3\2\2\2\35")
        buf.write("\"\5\6\4\2\36\"\5\b\5\2\37\"\5\n\6\2 \"\5\f\7\2!\35\3")
        buf.write("\2\2\2!\36\3\2\2\2!\37\3\2\2\2! \3\2\2\2\"#\3\2\2\2#!")
        buf.write("\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\5\16\b\2&\'\7\3\2\2\'\5")
        buf.write("\3\2\2\2()\5\26\f\2)*\7\4\2\2*+\7\5\2\2+,\5\30\r\2,-\7")
        buf.write("\6\2\2-\7\3\2\2\2./\5\26\f\2/\60\7\4\2\2\60\62\7\7\2\2")
        buf.write("\61\63\5\20\t\2\62\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2")
        buf.write("\2\2\64\65\3\2\2\2\65\t\3\2\2\2\66\67\5\26\f\2\678\7\4")
        buf.write("\2\289\7\b\2\29:\5\26\f\2:;\7\t\2\2;<\5\26\f\2<\13\3\2")
        buf.write("\2\2=>\5\26\f\2>?\7\4\2\2?@\7\n\2\2@A\5\26\f\2AC\7\13")
        buf.write("\2\2BD\5\22\n\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2")
        buf.write("\2FG\3\2\2\2GH\7\f\2\2H\r\3\2\2\2IJ\7\r\2\2JK\7\4\2\2")
        buf.write("KM\7\16\2\2LN\5\26\f\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2O")
        buf.write("P\3\2\2\2P\17\3\2\2\2QR\5\24\13\2RS\7\4\2\2ST\5\30\r\2")
        buf.write("TU\7\17\2\2U\21\3\2\2\2VW\7\20\2\2WX\5\24\13\2XY\7\21")
        buf.write("\2\2YZ\5\26\f\2Z^\7\22\2\2[]\7\21\2\2\\[\3\2\2\2]`\3\2")
        buf.write("\2\2^\\\3\2\2\2^_\3\2\2\2_\23\3\2\2\2`^\3\2\2\2ab\7\27")
        buf.write("\2\2b\25\3\2\2\2ce\7\23\2\2dc\3\2\2\2ef\3\2\2\2fd\3\2")
        buf.write("\2\2fg\3\2\2\2g\27\3\2\2\2hj\7\24\2\2ih\3\2\2\2jk\3\2")
        buf.write("\2\2ki\3\2\2\2kl\3\2\2\2l\31\3\2\2\2\n!#\64EO^fk")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'END'", "':'", "'PREGUNTA'", "'?'", "'RESPOSTA'", 
                     "'ITEM'", "'->'", "'ALTERNATIVA'", "'['", "']'", "'E'", 
                     "'ENQUESTA'", "';'", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "WORD", "WS", "LINE_COMMENT", "DIGIT" ]

    RULE_root = 0
    RULE_enquesta = 1
    RULE_pregunta = 2
    RULE_resposta = 3
    RULE_item = 4
    RULE_alternativa = 5
    RULE_definicioEnquesta = 6
    RULE_opcioResposta = 7
    RULE_opcioAlternativa = 8
    RULE_idopcio = 9
    RULE_identifier = 10
    RULE_text = 11

    ruleNames =  [ "root", "enquesta", "pregunta", "resposta", "item", "alternativa", 
                   "definicioEnquesta", "opcioResposta", "opcioAlternativa", 
                   "idopcio", "identifier", "text" ]

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
    T__15=16
    ID=17
    WORD=18
    WS=19
    LINE_COMMENT=20
    DIGIT=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enquesta(self):
            return self.getTypedRuleContext(EnquestesParser.EnquestaContext,0)


        def EOF(self):
            return self.getToken(EnquestesParser.EOF, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_root




    def root(self):

        localctx = EnquestesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.enquesta()
            self.state = 25
            self.match(EnquestesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnquestaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definicioEnquesta(self):
            return self.getTypedRuleContext(EnquestesParser.DefinicioEnquestaContext,0)


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
            return EnquestesParser.RULE_enquesta




    def enquesta(self):

        localctx = EnquestesParser.EnquestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enquesta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 27
                    self.pregunta()
                    pass

                elif la_ == 2:
                    self.state = 28
                    self.resposta()
                    pass

                elif la_ == 3:
                    self.state = 29
                    self.item()
                    pass

                elif la_ == 4:
                    self.state = 30
                    self.alternativa()
                    pass


                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.ID):
                    break

            self.state = 35
            self.definicioEnquesta()
            self.state = 36
            self.match(EnquestesParser.T__0)
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




    def pregunta(self):

        localctx = EnquestesParser.PreguntaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pregunta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.identifier()
            self.state = 39
            self.match(EnquestesParser.T__1)
            self.state = 40
            self.match(EnquestesParser.T__2)
            self.state = 41
            self.text()
            self.state = 42
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




    def resposta(self):

        localctx = EnquestesParser.RespostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_resposta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.identifier()
            self.state = 45
            self.match(EnquestesParser.T__1)
            self.state = 46
            self.match(EnquestesParser.T__4)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                self.opcioResposta()
                self.state = 50 
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




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.identifier()
            self.state = 53
            self.match(EnquestesParser.T__1)
            self.state = 54
            self.match(EnquestesParser.T__5)
            self.state = 55
            self.identifier()
            self.state = 56
            self.match(EnquestesParser.T__6)
            self.state = 57
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




    def alternativa(self):

        localctx = EnquestesParser.AlternativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_alternativa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.identifier()
            self.state = 60
            self.match(EnquestesParser.T__1)
            self.state = 61
            self.match(EnquestesParser.T__7)
            self.state = 62
            self.identifier()
            self.state = 63
            self.match(EnquestesParser.T__8)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.opcioAlternativa()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.T__13):
                    break

            self.state = 69
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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.IdentifierContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_definicioEnquesta




    def definicioEnquesta(self):

        localctx = EnquestesParser.DefinicioEnquestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_definicioEnquesta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(EnquestesParser.T__10)
            self.state = 72
            self.match(EnquestesParser.T__1)
            self.state = 73
            self.match(EnquestesParser.T__11)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.identifier()
                self.state = 77 
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

        def idopcio(self):
            return self.getTypedRuleContext(EnquestesParser.IdopcioContext,0)


        def text(self):
            return self.getTypedRuleContext(EnquestesParser.TextContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_opcioResposta




    def opcioResposta(self):

        localctx = EnquestesParser.OpcioRespostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opcioResposta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.idopcio()
            self.state = 80
            self.match(EnquestesParser.T__1)
            self.state = 81
            self.text()
            self.state = 82
            self.match(EnquestesParser.T__12)
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

        def idopcio(self):
            return self.getTypedRuleContext(EnquestesParser.IdopcioContext,0)


        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_opcioAlternativa




    def opcioAlternativa(self):

        localctx = EnquestesParser.OpcioAlternativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_opcioAlternativa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(EnquestesParser.T__13)
            self.state = 85
            self.idopcio()
            self.state = 86
            self.match(EnquestesParser.T__14)
            self.state = 87
            self.identifier()
            self.state = 88
            self.match(EnquestesParser.T__15)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.T__14:
                self.state = 89
                self.match(EnquestesParser.T__14)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdopcioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(EnquestesParser.DIGIT, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_idopcio




    def idopcio(self):

        localctx = EnquestesParser.IdopcioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idopcio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_identifier




    def identifier(self):

        localctx = EnquestesParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 97
                    self.match(EnquestesParser.ID)

                else:
                    raise NoViableAltException(self)
                self.state = 100 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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




    def text(self):

        localctx = EnquestesParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.match(EnquestesParser.WORD)
                self.state = 105 
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





