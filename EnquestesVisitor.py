from antlr4 import *
from EnquestesParser import EnquestesParser

class EnquestesVisitor(ParseTreeVisitor):
    
    def __init__(self):
        #per comprovar correctesa
        self.preguntes = {}
        self.respostes = {}
        self.items = {}
        self.arestesItems = {}
        self.alternatives = {}
        self.arestesAlternatives = {}
        
        #per crear el graf
        self.nodes = [] 
        self.arestes = []
    
    #Mètodes de creació i comprovació del graf
    
    def afegirPregunta(self, identificador, text):
        if identificador in self.preguntes: raise Exception('Error al intentar incloure una nova pregunta, l\'identificador està repetit: ' + identificador)
        else:
            self.preguntes[identificador] = True
            self.nodes.append((identificador, {'identificador': identificador, 'tipus': 'pregunta', 'text': text}))
            
    def afegirResposta(self, identificador):
        if identificador in self.respostes: raise Exception('Error al intentar incloure una nova resposta, l\'identificador està repetit: ' + identificador)
        else:
            self.respostes[identificador] = {}
            self.nodes.append((identificador, {'identificador': identificador, 'tipus': 'resposta'}))
            
    def afegirOpcioResposta(self, identificadorResposta, identificadorOpcioResposta, textOpcio):
        if identificadorOpcioResposta in self.respostes[identificadorResposta]: raise Exception('Error al intentar incloure una nova opció a la resposta ' + identificadorResposta + ', l\'identificador està repetit: ' + identificadorOpcioResposta)
        else:
            self.respostes[identificadorResposta][identificadorOpcioResposta] = True
            auxIdentificador = identificadorResposta + '-' + identificadorOpcioResposta
            self.nodes.append((auxIdentificador, {'identificadorResposta': identificadorResposta, 'identificadorOpcioResposta': identificadorOpcioResposta, 'tipus': 'opcioResposta', 'text': textOpcio}))
            self.arestes.append((identificadorResposta, auxIdentificador))

    def afegirItem(self, identificador, identificadorPregunta, identificadorResposta):
        if identificador in self.items: raise Exception('Error al intentar incloure una nou item, l\'identificador està repetit: ' + identificador)
        elif identificadorPregunta not in self.preguntes: raise Exception('Error al intentar incloure l\'item ' + identificador + ', no existeix la pregunta ' + identificadorPregunta)
        elif identificadorResposta not in self.respostes: raise Exception('Error al intentar incloure l\'item ' + identificador + ', no existeix la resposta ' + identificadorResposta)
        elif (identificadorPregunta+'-'+identificadorResposta) in self.arestesItems: raise Exception('Error al intentar incloure l\'item ' + identificador + ', ja existeix un altre item entre la mateix pregunta i resposta')
        else:
            self.arestesItems[identificadorPregunta+'-'+identificadorResposta] = True
            self.items[identificador] = {'pregunta': identificadorPregunta, 'resposta': identificadorResposta}
            self.arestes.append((identificadorPregunta, identificadorResposta, {'identificador': identificador}))
            
    def afegirDefinicioEnquesta(self, items):
        self.nodes.append(('E', {'identificador': 'E', 'tipus': 'enquesta'}))
        aux = {}
        priorItem = None
        for item in items:
            if item not in self.items: raise Exception('Error al intentar crear l\'enquesta, l\'identificador d\'item següent no existeix: ' + item)
            elif item in aux: raise Exception('Error al intentar crear l\'enquesta, l\'identificador d\'item següent apareix més d\'una vegada: ' + item)
            else:
                identificadorPregunta = self.items[item]['pregunta']
                if priorItem == None: 
                    self.arestes.append(('E',identificadorPregunta))
                else:
                    self.arestes.append((priorItem,identificadorPregunta))
                priorItem = identificadorPregunta
                
    def afegirAlternativa(identificador, identificadorItem, opcions):
        if identificador in self.alternatives: raise Exception('Error al intentar incloure una alternativa, l\'identificador està repetit: ' + identificador)
        elif identificadorItem not in self.items: raise Exception('Error al intentar incloure l\'alternativa ' + identificador + ', l\'item següent no existeix: ' + identificadorItem)
        for identificadorOpcioResposta, identificadorDesti in opcions:
            identificadorResposta = identificadorItem['resposta']
            if identificadorDesti not in self.items: raise Exception('Error al intentar incloure l\'alternativa ' + identificador + ', l\'item destí no existeix: ' + identificadorDesti)
            elif identificadorDesti == identificadorItem: raise Exception('Error al intentar incloure l\'alternativa ' + identificador + ', l\'item destí és igual a l\'orignal: ' + identificadorDesti)
            elif identificadorOpcioResposta not in self.respostes[identificadorResposta]: raise Exception('Error al intentar incloure l\'alternativa ' + identificador + ', l\'opció de resposta següent no existeix: ' + identificadorOpcioResposta)
            else:
                identificadorPregunta = identificadorItem['pregunta']
                identificadorPreguntaDesti = identificadorDesti['pregunta']
                if (identificadorPregunta+'-'+identificadorOpcioResposta) in self.arestesAlternatives: raise Exception('Error al intentar incloure l\'alternativa ' + identificador + ', l\'item ' + identificadorItem + ' ja té una alternativa amb l\'opció ' + identificadorOpcioResposta)
                else:
                    self.arestesAlternatives[identificadorPregunta+'-'+identificadorOpcioResposta] = True
                    self.arestes.append(identificadorPregunta, identificadorPreguntaDesti, {'identificador': identificadorOpcio})
            

    #Mètodes de visita
    
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        self.visitChildren(ctx)
        return self.nodes, self.arestes

    def visitPregunta(self, ctx:EnquestesParser.PreguntaContext):
        identificador = self.visit(ctx.identifier())
        text = self.visit(ctx.text())
        self.afegirPregunta(identificador,text)

    def visitResposta(self, ctx:EnquestesParser.RespostaContext):
        identificador = self.visit(ctx.identifier())
        self.afegirResposta(identificador)
        opcions = ctx.opcioResposta()
        for opcio in opcions:
            identificadorOpcio, text = self.visit(opcio)
            self.afegirOpcioResposta(identificador,identificadorOpcio,text)

    def visitItem(self, ctx:EnquestesParser.ItemContext):
        identificador = self.visit(ctx.identifier(0))
        identificadorPregunta = self.visit(ctx.identifier(1))
        identificadorResposta = self.visit(ctx.identifier(2))
        self.afegirItem(identificador,identificadorPregunta,identificadorResposta)

    def visitAlternativa(self, ctx:EnquestesParser.AlternativaContext):
        identificador = self.visit(ctx.identifier(0))
        identificadorItem = self.visit(ctx.identifier(1))
        opcions = ctx.opcioResposta()
        for opcio in opcions:
            identificadorOpcio, identificadorDesti = self.visit(opcio)
            self.afegirAlternativa(identificador, identificadorItem, identificadorOpcio, identificadorDesti)        

    def visitDefinicioEnquesta(self, ctx:EnquestesParser.DefinicioEnquestaContext):
        items = ctx.identifier()
        aux = []
        for item in items:
            aux.append(self.visit(item))
        self.afegirDefinicioEnquesta(aux)

    def visitOpcioResposta(self, ctx:EnquestesParser.OpcioRespostaContext):
        identifier = self.visit(ctx.identifierOpcio())
        text = self.visit(ctx.text())
        return identifier, text

    def visitOpcioAlternativa(self, ctx:EnquestesParser.OpcioAlternativaContext):
        identificadorOpcio = self.visit(ctx.identifierOpcio())
        identifier = self.visit(ctx.identifier())
        return identificadorOpcio, identifier

    def visitIdentifierOpcio(self, ctx:EnquestesParser.IdentifierOpcioContext):
        return ctx.getText()

    def visitIdentifier(self, ctx:EnquestesParser.IdentifierContext):
        return ctx.getText()

    def visitText(self, ctx:EnquestesParser.TextContext):
        return ctx.getText()
