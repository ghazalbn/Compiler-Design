import argparse
from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener


class CountOperations(JavaParserLabeledListener):
    def __init__(self):
        self.op_count = 0
        self.operations = {}

    def enterExpression10(self, ctx:JavaParserLabeled.Expression10Context):
        if ctx.SUB():
            self.operations['-'] = self.operations.get('-', 0) + 1
        else:
            self.operations['+'] = self.operations.get('+', 0) + 1
        self.op_count += 1

    def enterExpression9(self, ctx:JavaParserLabeled.Expression9Context):
        if ctx.MUL():
            self.operations['*'] = self.operations.get('*', 0) + 1
            self.op_count += 1
        elif ctx.DIV():
            self.operations['/'] = self.operations.get('/', 0) + 1
            self.op_count += 1


def extract_operations(file_path):

    if file_path.split('.')[-1] == 'java':
        stream = FileStream(r""+file_path, encoding="utf8")

        lexer = JavaLexer(stream)
        token_stream = CommonTokenStream(lexer)

        parser = JavaParserLabeled(token_stream)
        tree = parser.compilationUnit()

        listener = CountOperations()
        walker = ParseTreeWalker()

        walker.walk(listener, tree)

    return listener.operations, listener.op_count


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Java operation counter')
    arg_parser.add_argument(
        '-n', '--file',
        help='Java file path',
        default=r"Game.java"
    )
    args = arg_parser.parse_args()
    operations, op_count = extract_operations(args.file)
    print('operations:', operations)
    print('all operations count:', op_count)
