import argparse
import os
from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener


class FindStatement(JavaParserLabeledListener):
    def __init__(self):
        self.statements = []

    def enterExpression20(self, ctx: JavaParserLabeled.Expression20Context):
        id = ctx.parentCtx.start.start
        start = ctx.start.start
        stop = ctx.stop.stop
        # a = ctx.parentCtx.ASSIGN().symbol.start
        q = ctx.QUESTION().symbol.start
        c = ctx.COLON().symbol.start
        self.statements.append((start, q, c, stop, id))


def refactor(file_path, out_path):

    if file_path.split('.')[-1] == 'java':
        stream = FileStream(r""+file_path, encoding="utf8")

        if os.path.exists(out_path):
            os.remove(out_path)
        output_stream = open(r"" + out_path, "a")

        lexer = JavaLexer(stream)
        token_stream = CommonTokenStream(lexer)

        parser = JavaParserLabeled(token_stream)
        tree = parser.compilationUnit()

        listener = FindStatement()
        walker = ParseTreeWalker()

        walker.walk(listener, tree)
        statements = listener.statements

        text = stream.strdata
        d = 0
        refactored = text
        for statement in statements:
            start, q, c, stop, id = statement
            if_else = f"""if ({text[start:q]})
        {{
            {text[id:start]}{text[q+1:c]};
        }}
        else 
        {{
            {text[id:start]}{text[c+1:stop+1]};
        }}"""
            refactored = refactored[:id+d] + if_else + refactored[stop+2+d:]
            d += len(if_else) - stop + id - 2

        output_stream.write(refactored)
        output_stream.close()

        output_stream = open(r"" + out_path, "r")
        print(*output_stream.readlines())
        output_stream.close()


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Java Refactor If Else Statements')
    arg_parser.add_argument(
        '-n', '--file',
        help='input java file path',
        default=r"Game.java"
    )
    arg_parser.add_argument(
        '-out', '--out',
        help='output java file path',
        default=r"GameRefactored.java"
    )
    args = arg_parser.parse_args()
    refactor(args.file, args.out)
