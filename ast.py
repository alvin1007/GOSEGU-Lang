class Program:
    def __init__(self) -> None:
        self.Statements = []
        
    def TokenLiteral(self) -> str:
        if len(self.Statements) > 0:
            return self.Statements[0].TokenLiteral()
        else:
            return ""
    
    def String(self) -> str:
        out = ""
        for stmt in self.Statements:
            out += stmt.String()
        return out

#
# Statement = { TokenLiteral(), String() }
#

class ExpressionStatement:
    def __init__(self, Token) -> None:
        self.Token = Token # 표현식의 첫 번째 토큰
        self.Expression = ""

    def TokenLiteral(self) -> str:
        return self.Token['Literal']

    def String(self) -> str:
        if self.Expression:
            return self.Expression.String()
        return ""

#
# Expression = { TokenLiteral(), String() }
#

class InfixExpression:
    def __init__(self, Token, Operator, Left) -> None:
        self.Token = Token
        self.Left = Left
        self.Operator = Operator
        self.Right = ""
    
    def TokenLiteral(self) -> str:
        return self.Token['Literal']

    def String(self) -> str:
        return "(" + self.Left.String() + " " + self.Operator + " " + self.Right.String() + ")"

class IntegerLiteral:
    def __init__(self, Token, Value) -> None:
        self.Token = Token
        self.Value = Value
    
    def TokenLiteral(self) -> str:
        return self.Token['Literal']
    
    def String(self) -> str:
        return self.Token['Literal']
