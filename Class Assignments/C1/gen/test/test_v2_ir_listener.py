"""
Example of three address code generator

"""
from gen.test.v2_python.test_v2Parser import test_v2Parser
from gen.test.v2_python.test_v2Listener import test_v2Listener

class DummyListener(test_v2Listener):

    def exitExpr1(self, ctx:test_v2Parser.Expr1Context):
        print('I enter plus with first operand {0} second operand {1}:'.format(ctx.expr().getText(), ctx.term().getText()))





class TreeAddressCode(test_v2Listener):
    """
        Generate three address code for part of expression rule of CPP14 grammar
    """

    def __init__(self):
        self.temp_counter = 0
        # self.value = 0

    def create_temp(self):
        self.temp_counter += 1
        return 'T' + str(self.temp_counter)

    def remove_temp(self):
        self.temp_counter -= 1

    def get_temp(self):
        return 'T' + str(self.temp_counter)

    # Rule: #fact1
    def exitFact1(self, ctx: test_v2Parser.Fact1Context):
        ctx.code = ctx.getText()

    def exitFact2(self, ctx: test_v2Parser.Fact2Context):
        ctx.code = ctx.getText()

    def exitFact3(self, ctx: test_v2Parser.Fact3Context):
        ctx.code = ctx.expr().code

    def exitTerm1(self, ctx: test_v2Parser.Term1Context):
        temp = self.create_temp()
        print(temp, '=', ctx.term().code, '*', ctx.fact().code)
        ctx.code = temp

        # self.value = int(ctx.term().code) * int(ctx.fact().code)
        # ctx.code = self.value

    def exitTerm2(self, ctx: test_v2Parser.Term1Context):
        temp = self.create_temp()
        print(temp, '=', ctx.term().code, '/', ctx.fact().code)
        ctx.code = temp

        # self.value = int(ctx.term().code) / int(ctx.fact().code)
        # ctx.code = self.value

    def exitTerm3(self, ctx: test_v2Parser.Term3Context):
        ctx.code = ctx.fact().code

    def exitExpr1(self, ctx: test_v2Parser.Expr1Context):
        temp = self.create_temp()
        print(temp, '=', ctx.expr().code, '+', ctx.term().code)
        ctx.code = temp

        # self.value = int(ctx.expr().code) + int(ctx.term().code)
        # ctx.code = self.value

    def exitExpr2(self, ctx: test_v2Parser.Expr1Context):
        temp = self.create_temp()
        print(temp, '=', ctx.expr().code, '-', ctx.term().code)
        ctx.code = temp

        # self.value = int(ctx.expr().code) - int(ctx.term().code)
        # ctx.code = self.value

    def exitExpr3(self, ctx: test_v2Parser.Expr1Context):
        ctx.code = ctx.term().code

    def exitStart(self, ctx: test_v2Parser.StartContext):
        # pass
        print(ctx.Id(), '=', ctx.expr().code)
        # print(ctx.Id(), '=', self.value)
