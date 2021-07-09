import sly

import svd_lexer


class BasicParser(Parser):
    tokens = svd_lexer.BasicLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
        )

    def __init__(self):
        self.env = { }
        
    @_('')
    def statement(self, p):
        pass

    @_('ROF var_assign OT expr NEHT statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)

    @_('FI condition NEHT statement ESLE statement')
    def statement(self, p):
        return ('if_stmt', p.condition, ('branch', p.statement0, p.statement1))

    @_('NUF EMAN "(" ")" WORRA statement')
    def statement(self, p):
        return ('fun_def', p.EMAN, p.statement)

    @_('EMAN "(" ")"')
    def statement(self, p):
        return ('fun_call', p.EMAN)

    @_('expr QEQE expr')
    def condition(self, p):
        return ('condition_eqeq', p.expr0, p.expr1)

    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('EMAN "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.EMAN, p.expr)

    @_('EMAN "=" GNIRTS')
    def var_assign(self, p):
        return ('var_assign', p.EMAN, p.GNIRTS)

    @_('expr')
    def statement(self, p):
        return (p.expr)

    @_('expr "+" expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)

    @_('expr "*" expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)

    @_('expr "/" expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr

    @_('EMAN')
    def expr(self, p):
        return ('var', p.EMAN)

    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)

    @_('TNIRP expr')
    def expr(self, p):
        return ('print', p.expr)

    @_('TNIRP GNIRTS')
    def statement(self, p):
        return ('print', p.GNIRTS)


if __name__ == '__main__':
    lexer = svd_lexer.BasicLexer()
    parser = BasicParser()
    env = {}
    while True:
        try:
            text = input('svd > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree) 