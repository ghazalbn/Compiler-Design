from typing import List

from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from gen.XMLParserListener import XMLParserListener

_attributes_factory = {
    "geometry": "{obj_name}.setGeometry({value})\n",
    "maximum": "{obj_name}.setMaximum({value})\n",
    "minimum": "{obj_name}.setMinimum({value})\n",
    "prefix": "{obj_name}.setPrefix('{value}')\n",
    "range": "{obj_name}.setRange({value})\n",

}


class attribute:
    def __init__(self, root, attr):
        self.tag = root
        self.value = attr

    def __str__(self):
        return f"{self.tag} = {self.value}"

    def __repr__(self):
        return self.__str__()


class ast_creator(XMLParserListener):

    def __init__(self):
        self.root = ''
        self.attrs = []

    def enterElement(self, ctx: XMLParser.ElementContext):
        self.root = ctx.Name(0)

    def enterAttribute(self, ctx: XMLParser.AttributeContext):
        tag, value = ctx.Name().getText(), ctx.STRING().getText()
        at = attribute(tag, value)
        self.attrs.append(at)

    def show_tree(self):
        print(f"  {self.root}")

        temp_str = ""
        for at in self.attrs:
            temp_str += at.tag + " " * 15
        print(temp_str)
        temp_str = ""
        for at in self.attrs:
            temp_str += at.value + " " * 15
        print(temp_str)


def get_ast_str(ast_list: List[ast_creator], obj_name='DSB', start_str="", num_of_space=0):
    indent = " " * num_of_space
    for ast in ast_list:
        output_code = f"{indent}{obj_name} = QDoubleSpinBox()\n"
        for at in ast.attrs:
            tag = at.tag
            val = at.value
            at_str = indent+_attributes_factory[tag].format(obj_name=obj_name, value=f"{val[1:-1]}")
            output_code += at_str
        start_str += output_code
    return start_str
