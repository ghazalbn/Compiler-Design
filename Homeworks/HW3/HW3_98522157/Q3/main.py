from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from AST import ast_creator, get_ast_str

file_name = input("Enter java name: ")
input_stream = FileStream(fileName=file_name)
lexer = JavaLexer(input_stream)

stream = CommonTokenStream(lexer)
parser = JavaParserLabeled(stream)
tree = parser.document()

listener = ast_creator()
walker = ParseTreeWalker()
walker.walk(listener, tree)
listener.show_tree()
print(f"root: {listener.root}, attrs: {listener.attrs}")