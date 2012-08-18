#  Copyright (c) 1998-2000 John Aycock
#  
#  Permission is hereby granted, free of charge, to any person obtaining
#  a copy of this software and associated documentation files (the
#  "Software"), to deal in the Software without restriction, including
#  without limitation the rights to use, copy, modify, merge, publish,
#  distribute, sublicense, and/or sell copies of the Software, and to
#  permit persons to whom the Software is furnished to do so, subject to
#  the following conditions:
#  
#  The above copyright notice and this permission notice shall be
#  included in all copies or substantial portions of the Software.
#  
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#
#	The contents of this file are basically just 
#	cut-and-pasted straight from the paper.
#

from spark import GenericScanner, GenericParser
from ast import AST, ASTTraversal
from token import Token

#
#	SCANNING
#

class SimpleScanner(GenericScanner):
    def __init__(self):
        GenericScanner.__init__(self)
    
    def tokenize(self, input):
        self.rv = []
        GenericScanner.tokenize(self, input)
        return self.rv
    
    def t_whitespace(self, s):
        r' \s+ '
        pass
        
    def t_op(self, s):
        r' \+ | \* '
        self.rv.append(Token(type=s))
        
    def t_number(self, s):
        r' \d+ '
        t = Token(type='number', attr=s)
        self.rv.append(t)

    def t_string(self, s):
        r' "[^"]*" '
        t = Token(type='string', attr=s)
        self.rv.append(t)
#
#	PARSING
#

class ExprParser(GenericParser):
    def __init__(self, start='expr'):
        GenericParser.__init__(self, start)
                
    def p_expr_1(self, args):
        ' expr ::= expr + term '
        return AST(type=args[1],
                   left=args[0],
                   right=args[2])
        
    def p_expr_2(self, args):
        ' expr ::= term '
        return args[0]
        
    def p_term_1(self, args):
        ' term ::= term * factor '
        return AST(type=args[1],
                   left=args[0],
                   right=args[2])
        
    def p_term_2(self, args):
        ' term ::= factor '
        return args[0]
        
    def p_factor_1(self, args):
        ' factor ::= number '
        return AST(type=args[0])

    def p_factor_2(self, args):
        ' factor ::= string '
        return AST(type=args[0])

def parse(tokens):
    parser = ExprParser()
    return parser.parse(tokens)

#
#	SEMANTIC CHECKING
#

class TypeCheck(ASTTraversal):
    def __init__(self, ast):
        ASTTraversal.__init__(self, ast)
        self.postorder()
        
    def n_number(self, node):
        node.exprType = 'number'
        
    def n_string(self, node):
        node.exprType = 'string'
        
    def default(self, node):
        # this handles + and * nodes
        leftType = node.left.exprType
        rightType = node.right.exprType
        if node.type == '*':
            if leftType == 'string' and rightType == 'string':
                raise TypeError
            if leftType == 'string' or rightType == 'string':
                node.exprType = 'string'
            else:
                node.exprType = 'number'
        else:
            if leftType != rightType:
                raise TypeError
            node.exprType = leftType

def semantic(ast):
    TypeCheck(ast)
    #
    #  Any other ASTTraversal classes
    #  for semantic checking would be
    #  instantiated here...
    #
    return ast

#
#	CODE GENERATION
#

class Interpret(ASTTraversal):
    def __init__(self, ast):
        ASTTraversal.__init__(self, ast)
        self.postorder()
        
    def n_number(self, node):
        node.value = int(node.attr)
        
    def n_string(self, node):
        node.value = node.attr[1:-1]
        
    def default(self, node):
        left = node.left.value
        right = node.right.value
        
        if node.type == '+':
            node.value = left + right
        else:
            node.value = left * right

def generate(ast):
	Interpret(ast)
	return ast

def simplecalc(expr):
    return  generate(semantic(parse(scan_expr(expr))))
#
#	MAIN
#
def scan_expr(input):
    scanner = SimpleScanner()
    return scanner.tokenize(input)

if __name__ == '__main__':
        expr = "2 + 3 * 5"
	ast = simplecalc(expr)
        print ast.value
