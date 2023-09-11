# Generated from D:/uni/compiler/assignments/HW1/HW1_98522157/grammars\Cow.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CowParser import CowParser
else:
    from CowParser import CowParser

# This class defines a complete listener for a parse tree produced by CowParser.
class CowListener(ParseTreeListener):

    # Enter a parse tree produced by CowParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CowParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CowParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CowParser.CompilationUnitContext):
        pass



del CowParser