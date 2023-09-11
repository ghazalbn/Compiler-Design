"""
feature QDoubleSpinBox
"""
import os
import argparse
from typing import List

from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from AST import ast_creator, get_ast_str

file_name = input("Enter xml file name: ")
input_stream = FileStream(fileName=file_name)
lexer = XMLLexer(input_stream)

tokens = lexer.getAllTokens()
i = 0
q_box_spin_texts = []
while i < len(tokens):
    t = tokens[i]
    if t.text.lower() == "qdoublespinbox":
        s = "<QDoubleSpinBox "
        i += 1
        t = tokens[i]
        while t.type != lexer.SLASH_CLOSE:
            s += f" {t.text}"

            i += 1
            t = tokens[i]
        s += f" {t.text}"
        q_box_spin_texts.append(s)
    i += 1

ast_list = []
for box in q_box_spin_texts:
    input_s = InputStream(box)
    lexer = XMLLexer(input_s)

    stream = CommonTokenStream(lexer)
    parser = XMLParser(stream)
    tree = parser.document()

    listener = ast_creator()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    ast_list.append(listener)
    listener.show_tree()
    print(f"root: {listener.root}, attrs: {listener.attrs}")

python_output = """
# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
 
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Python ")
  
        # setting geometry
        self.setGeometry(100, 100, 500, 400)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for components
    def UiComponents(self):
"""

python_output = get_ast_str(ast_list, start_str=python_output, num_of_space=8)
python_output +="""
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())
"""
print(python_output)

with open("python_output.py", 'w') as f:
    f.write(python_output)
