# Generated from D:/uni/compiler/assignments/HW1/HW1_98522157/grammars\Cow.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,56,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,44,8,0,
        1,1,1,1,1,1,1,1,1,2,4,2,51,8,2,11,2,12,2,52,1,2,1,2,0,0,3,1,1,3,
        2,5,3,1,0,1,3,0,9,9,13,13,32,32,67,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,1,43,1,0,0,0,3,45,1,0,0,0,5,50,1,0,0,0,7,8,5,109,0,0,8,9,5,
        111,0,0,9,44,5,111,0,0,10,11,5,109,0,0,11,12,5,111,0,0,12,44,5,79,
        0,0,13,14,5,109,0,0,14,15,5,79,0,0,15,44,5,111,0,0,16,17,5,109,0,
        0,17,18,5,79,0,0,18,44,5,79,0,0,19,20,5,77,0,0,20,21,5,111,0,0,21,
        44,5,111,0,0,22,23,5,77,0,0,23,24,5,111,0,0,24,44,5,79,0,0,25,26,
        5,77,0,0,26,27,5,79,0,0,27,44,5,111,0,0,28,29,5,77,0,0,29,30,5,79,
        0,0,30,44,5,79,0,0,31,32,5,79,0,0,32,33,5,79,0,0,33,44,5,79,0,0,
        34,35,5,77,0,0,35,36,5,77,0,0,36,44,5,77,0,0,37,38,5,79,0,0,38,39,
        5,79,0,0,39,44,5,77,0,0,40,41,5,111,0,0,41,42,5,111,0,0,42,44,5,
        109,0,0,43,7,1,0,0,0,43,10,1,0,0,0,43,13,1,0,0,0,43,16,1,0,0,0,43,
        19,1,0,0,0,43,22,1,0,0,0,43,25,1,0,0,0,43,28,1,0,0,0,43,31,1,0,0,
        0,43,34,1,0,0,0,43,37,1,0,0,0,43,40,1,0,0,0,44,2,1,0,0,0,45,46,5,
        10,0,0,46,47,1,0,0,0,47,48,6,1,0,0,48,4,1,0,0,0,49,51,7,0,0,0,50,
        49,1,0,0,0,51,52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,
        0,54,55,6,2,1,0,55,6,1,0,0,0,3,0,43,52,2,6,0,0,0,1,0
    ]

class CowLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Instruction = 1
    Newline = 2
    Whitespace = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "Instruction", "Newline", "Whitespace" ]

    ruleNames = [ "Instruction", "Newline", "Whitespace" ]

    grammarFileName = "Cow.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


