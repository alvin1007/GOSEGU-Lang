import ast
import object

# Eval { ast.Node } -> object
def Eval(node):
    match type(node):
        case ast.Program:
            return evalStatements(node)
        case ast.ExpressionStatement:
            return Eval(node.Expression)
        case ast.InfixExpression:
            left = Eval(node.Left)
            right = Eval(node.Right)
            return evalInfixExpression(node.Operator, left, right)
        case ast.IntegerLiteral:
            return object.Integer(node.Value)
        case _:
            return object.NULL

def evalStatements(node):
    for statement in node.Statements:
        result = Eval(statement)

    return result

def evalInfixExpression(operator:str, left, right):
    if left.Type() == object.INTEGER_OBJECT and right.Type() == object.INTEGER_OBJECT:
        return evalIntegerInfixExpression(operator, left, right)
    else:
        return object.NULL

def evalIntegerInfixExpression(operator:str, left, right):
    match operator:
        case "+":
            return object.Integer(left.Value + right.Value)
        case "-":
            return object.Integer(left.Value - right.Value)
        case "*":
            return object.Integer(left.Value * right.Value)
        case "/":
            return object.Integer(left.Value / right.Value)
        case "%":
            return object.Integer(left.Value % right.Value)
        case _:
            return object.NULL