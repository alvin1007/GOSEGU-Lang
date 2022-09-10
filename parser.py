import token
from typing import Dict
import lexer
import ast

class Parser:

    priority:Dict[str, int] = {
        "LOWEST":1,
        "EQUALS":2,
        "LESSGREATER":3,
        "SUM":4,
        "PRODUCT":5,
        "PREFIX":6,
        "CALL":7
    }

    precedences:Dict[str, int] = {
        token.PLUS: priority["SUM"],
        token.MINUS: priority["SUM"],
        token.SLASH: priority["PRODUCT"],
        token.ASTERISK: priority["PRODUCT"]
    }

    def __init__(self, l:lexer.Lexer) -> None:
        self.l = l

        self.curToken = {}
        self.peekToken = {}

        self.prefixParseFns: Dict[str, function] = {}
        self.registerPrefix(token.INT, self.parseIntegerLiteral)

        self.infixParseFns: Dict[str, function] = {}
        self.registerInfix(token.PLUS, self.parseInfixExpression)
        self.registerInfix(token.MINUS, self.parseInfixExpression)
        self.registerInfix(token.ASTERISK, self.parseInfixExpression)
        self.registerInfix(token.SLASH, self.parseInfixExpression)
        self.registerInfix(token.REMAINDER, self.parseInfixExpression)

        self.nextToken()
        self.nextToken()
    
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.l.NextToken()

    def registerPrefix(self, tokenType:str, fn) -> None:
        self.prefixParseFns[tokenType] = fn
    
    def registerInfix(self, tokenType:str, fn) -> None:
        self.infixParseFns[tokenType] = fn
    
    def parseProgram(self) -> ast.Program:
        program = ast.Program()

        while self.curToken['Token'] != token.EOF:
            stmt = self.parseStatement()
            if stmt:
                program.Statements.append(stmt)
            self.nextToken()
        
        return program
            
    def parseStatement(self):
        match self.curToken['Token']:
            case _:
                return self.parseExpressionStatement()
    
    def parseExpressionStatement(self) -> ast.ExpressionStatement:
        stmt = ast.ExpressionStatement(self.curToken)
        stmt.Expression = self.parseExpression(self.priority['LOWEST'])

        if self.peekTokenIs(token.EOF):
            self.nextToken()

        return stmt

    # Return Expression
    def parseExpression(self, precedence:int):
        prefix = self.prefixParseFns[self.curToken['Token']]
        if not prefix:
            return
        leftExp = prefix()

        while not self.peekTokenIs(token.EOF) and precedence < self.peekPrecedence():
            infix = self.infixParseFns[self.peekToken['Token']]
            if not infix:
                return leftExp
            self.nextToken()
            leftExp = infix(leftExp)

        return leftExp

    def parseInfixExpression(self, left) -> ast.InfixExpression:
        exp = ast.InfixExpression(self.curToken, self.curToken['Literal'], left)
        precedence = self.curPrecedence()
        self.nextToken()
        exp.Right = self.parseExpression(precedence)
        return exp

    def parseIntegerLiteral(self) -> ast.IntegerLiteral:
        val = int(self.curToken['Literal'])
        lit = ast.IntegerLiteral(self.curToken, val)

        return lit

    def curTokenIs(self, t:str) -> bool:
        return self.curToken['Token'] == t
        
    def peekTokenIs(self, t:str) -> bool:
        return self.peekToken['Token'] == t

    def curPrecedence(self) -> int:
        p = self.precedences[self.curToken['Token']]
        if p:
            return p
        return self.priority['LOWEST']

    def peekPrecedence(self) -> int:
        p = self.precedences[self.peekToken['Token']]
        if p:
            return p
        return self.priority['LOWEST']

