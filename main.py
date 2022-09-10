import parser
import lexer
import eval

test = """10 + 4 * 2 - 9"""

if __name__ == '__main__':
    print("""GOSEGU Lang 1.0\n""")
    while True:
        print(">>", end="")
        Text = input()
        if Text == "":
            break
        l = lexer.Lexer(Text)
        p = parser.Parser(l)
        program = p.parseProgram()
        print("킹-아!   ", end="")
        print(eval.Eval(program).Value)
