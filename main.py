import parser
import lexer

test = """1 + 2 * 5 - 1023 / 4 + 213 * 10 + 4 / 3 / 21"""

if __name__ == '__main__':
    l = lexer.Lexer(test)
    p = parser.Parser(l)
    program = p.parseProgram()
    print(program.String())