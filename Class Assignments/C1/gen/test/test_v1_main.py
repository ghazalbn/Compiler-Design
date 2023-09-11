from antlr4 import *

from v1_python.testLexer import testLexer
from v1_python.testParser import testParser

# Step 0: Input program
# input_string = 'y = a + b * c -'
input_string = """y& = a? + b% * c# / er$@ - // line comment
/*block
comment*/"""
# Step 1: Convert input to stream
stream = InputStream(input_string)
# Step 2: Create lexer object
lexer = testLexer(stream)
# Step 3: Create a token stream
token_stream = CommonTokenStream(lexer)
# Step 4: Create a parser object
parser = testParser(token_stream)
# Step 5: Parse from start rule
parse_tree = parser.start()

lexer.reset()
for i, token in enumerate(lexer.getAllTokens()):
    # print(token)
    print(
        f"token {i}:\n",
        f"token: {token.text}\n",
        f"token length: {len(token.text)}\n",
        f"token type number: {token.type}\n",
        f"token type rule name: {testLexer.ruleNames[token.type - 1]}\n"
    )
