from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener
import queue

class attribute:
    def __init__(self, root, attr):
        self.ast = AST().root
        self.q = queue.Queue()

    def __repr__(self):
        return self.__str__()

class ast_creator(JavaParserLabeledListener):

    def __init__(self):
        self.root = ''
        self.q = []

    def enterElement(self, ctx: JavaParserLabeled.ElementContext):
        self.root = ctx.Name(0)

    def enterAttribute(self, ctx: JavaParserLabeled.AttributeContext):
        ast, value = ctx.Name().getText(), ctx.STRING().getText()
        at = attribute(ast, value)
        self.q.append(at)

    def show_tree(self):
        print(f"  {self.root}")

        temp_str = ""
        for at in self.q:
            temp_str += at.ast + " " * 15
        print(temp_str)
        temp_str = ""
        for at in self.q:
            temp_str += at.value + " " * 15
        print(temp_str)



class AST:
    def __init__(self):
        self.root = None
        self.current = None
        self.q = queue.Queue()

    def make_node(self, value, child, brother):
        tree_node = Node(value, child, brother)
        if self.root is None:
            self.root = tree_node
            self.current = tree_node
        return tree_node

    def add_child(self, node, new_child):
        if node.child is None:
            node.child = new_child
        else:
            self.current = node.child
            while self.current.brother is not None:
                self.current = self.current.brother
            self.current.brother = new_child
        self.current = new_child

    def add_brother(self, node, new_brother):
        if node.brother is None:
            node.brother = new_brother
        else:
            self.current = node.brother
            while self.current.brother is not None:
                self.current = self.current.brother
            self.current.brother = new_brother
        self.current = new_brother

    def print_tree(self, node=None, level=1):
        if node is None:
            print("--------Finished----------")
            return
        if not self.q.empty():
            print('Parent:', self.q.get().value)
            print('\t'*level, end='')
        while node is not None:
            print(node.value, '\t───\t', end='')  # alt+196 = ───, alt+178=▓
            if node.child is not None:
                self.q.put(node.child)
                self.q.put(node)
            node = node.brother
            if node is None:
                print('▓', end='\n')
        if not self.q.empty():
            self.print_tree(node=self.q.get(), level=level + 1)


class Node:
    def __init__(self, value, child, brother):
        self.value = value
        self.child = child
        self.brother = brother

