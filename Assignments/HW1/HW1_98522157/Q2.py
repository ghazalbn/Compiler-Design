import argparse
from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener


class FindMethods(JavaParserLabeledListener):
    def __init__(self):
        self.methods = []
        self.class_name = ""
        self.classes_tuple = []

    def enterMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        self.methods.append(str(ctx.IDENTIFIER()))

    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        self.class_name = str(ctx.IDENTIFIER())

    def exitClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        self.classes_tuple.append((self.class_name, self.methods))
        self.methods = []


def extract_methods(file_path):

    if file_path.split('.')[-1] == 'java':
        stream = FileStream(r""+file_path, encoding="utf8")

        lexer = JavaLexer(stream)
        token_stream = CommonTokenStream(lexer)

        parser = JavaParserLabeled(token_stream)
        tree = parser.compilationUnit()

        listener = FindMethods()
        walker = ParseTreeWalker()

        walker.walk(listener, tree)

    return listener.classes_tuple


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Java class methods extractor')
    arg_parser.add_argument(
        '-n', '--file',
        help='Java file path',
        default=r"Game.java"
    )
    args = arg_parser.parse_args()
    class_methods = extract_methods(args.file)
    print(class_methods)
