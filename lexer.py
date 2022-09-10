import token

class Lexer:
    def __init__(self, input: str) -> None:
        self.input = input
        self.position = 0
        self.readPosition = 0
        self.ch = ""
        self.line = 1
        self.readChar()

    def TestStart(self) -> None:
        while True: 
            l = self.NextToken()
            print(l)
            if l['Token'] == token.EOF:
                break

    #return token
    def NextToken(self) -> dict:
        self.skipWhiteSpace()
        match self.ch:
            case "+":
                tok = token.PLUS
                lit = self.ch
                lin = self.line
            case "-":
                tok = token.MINUS
                lit = self.ch
                lin = self.line
            case "*":
                tok = token.ASTERISK
                lit = self.ch
                lin = self.line
            case "/":
                tok = token.SLASH
                lit = self.ch
                lin = self.line
            case "%":
                tok = token.REMAINDER 
                lit = self.ch
                lin = self.line
            case "":
                tok = token.EOF
                lit = ""
                lin = self.line
            case _:
                if self.isDigit(self.ch):
                    return {
                        'Token': token.INT,
                        'Literal' : self.readNumber(),
                        'Line': self.line
                    }
                else:
                    return {
                        'Token': token.ILLEGAL,
                        'Literal' : "",
                        'Line': self.line
                    }
        self.readChar()

        return {
            'Token': tok,
            'Literal': lit,
            'Line': lin
        }
    
    def readChar(self) -> None:
        if self.readPosition >= len(self.input):
            self.ch = ""
        else:
            self.ch = self.input[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1

    def readNumber(self) -> str:
        position = self.position
        while self.isDigit(self.ch):
            self.readChar()
        return self.input[position:self.position]

    def skipWhiteSpace(self) -> None:
        while self.ch == "\n" or self.ch == " " or self.ch == "\t" or self.ch == "\r":
            self.readChar()
    
    def isDigit(self, ch:str) -> bool:
        return "0" <= ch and ch <= "9"
    