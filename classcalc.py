#!/usr/bin/env python

# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
#
# Class-based example contributed to PLY by David McNab
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input

import ply.lex as lex
import ply.yacc as yacc
import os

class Parser:
    """
    Base class for a lexer/parser that has the rules defined as methods
    """
    tokens = ()
    precedence = ()
    reserved = {}

    def __init__(self, **kw):
        self.debug = kw.get('debug', 0)
        self.names = { }
        self.result = []
        try:
            modname = os.path.split(os.path.splitext(__file__)[0])[1] + "_" + self.__class__.__name__
        except:
            modname = "parser"+"_"+self.__class__.__name__
        self.debugfile = modname + ".dbg"
        self.tabmodule = modname + "_" + "parsetab"
        #print self.debugfile, self.tabmodule

        # Build the lexer and parser
        lex.lex(module=self, debug=self.debug)
        yacc.yacc(module=self,
                  debug=self.debug,
                  debugfile=self.debugfile,
                  tabmodule=self.tabmodule)

    def run(self):
        while 1:
            try:
                s = raw_input('calc > ')
            except EOFError:
                break
            if not s: continue
            yacc.parse(s)

    def run_string(self, s):
        yacc.parse(s)
        
    
class Calc(Parser):

    reserved = {
        'add' : 'ADD',
        'mul' : 'MUL'
        }

    tokens = [
        'NAME','INT','FLOAT','STRING',
        'LPAREN','RPAREN',
        'DOT'
        ] + list(reserved.values())

    # Tokens

    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_DOT     = r'\.'

    def t_FLOAT(self, t):
        r'\d+\.\d*|\.\d+'
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r'\d+'
        try:
            t.value = int(t.value)
        except ValueError:
            print("Integer value too large %s" % t.value)
            t.value = 0
        #print "parsed number %s" % repr(t.value)
        return t

    def t_STRING(self, t):
        r'"[^"]*"'
        t.value = t.value[1:-1]
        return t

    def t_NAME(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'NAME')
        return t

    t_ignore = " \t"

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")
    
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Parsing rules

    precedence = ()

    def p_statement_expr(self, p):
        'statement : expression'
        self.result.append(p[1])

    def p_expression_group(self, p):
        'expression : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_expression_literal(self, p):
        """
        expression : INT
                   | FLOAT
                   | STRING
        """
        p[0] = p[1]

    def p_func(self, p):
        """
        func : ADD
             | MUL
        """
        p[0] = p[1]

    def p_expression_method(self, p):
        'expression : expression DOT func LPAREN expression RPAREN'
        p[0] = p[1] #stub

    def p_expression_name(self, p):
        'expression : NAME'
        try:
            p[0] = self.names[p[1]]
        except LookupError:
            print("Undefined name '%s'" % p[1])
            p[0] = 0

    def p_error(self, p):
        if p:
            print("Syntax error at '%s'" % p.value)
        else:
            print("Syntax error at EOF")

if __name__ == '__main__':
    calc = Calc()
    calc.run()
