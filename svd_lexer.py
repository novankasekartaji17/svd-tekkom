
from sly import Lexer


class BasicLexer(Lexer):
    tokens = { EMAN, NUMBER, GNIRTS, TNIRP, FI, NEHT, ESLE, ROF, NUF, OT, WORRA, QEQE, COMMENT }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    TNIRP = r'TAMPIL'
    FI = r'JIKA'
    NEHT = r'MAKA'
    ESLE = r'LAIN'
    ROF = r'UNTUK'
    NUF = r'FUNGSI'
    OT = r'SAMPAI'
    WORRA = r'->'
    EMAN = r'[a-zA-Z_][a-zA-Z0-9_]*'
    GNIRTS = r'\".*?\"'

    QEQE = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')


if __name__ == '__main__':
    lexer = BasicLexer()
    env = {}
    while True:
        try:
            text = input('svd > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)