import argparse
import os
from antlr4 import *
from gen.JavaLexer import JavaLexer
from antlr4.TokenStreamRewriter import TokenStreamRewriter


def refactor(file_path, out_path):

    if file_path.split('.')[-1] == 'java':
        stream = FileStream(r""+file_path, encoding="utf8")

        lexer = JavaLexer(stream)

        if os.path.exists(out_path):
            os.remove(out_path)
        output_stream = open(r"" + out_path, "a")

        token = lexer.nextToken()
        pre_token = token
        while token.type != Token.EOF:
            text = token.text
            if token.type in [lexer.LINE_COMMENT, lexer.COMMENT]:
                # if token.type == lexer.LINE_COMMENT:
                #     text = f'/*{name} {number}\n{token.text[2:]}*/'
                if token.type == lexer.COMMENT:
                    if text.__contains__('\n'):
                        ind = text.index('\n')
                        text = f'//{token.text[2:ind]}'
                    else:
                        text = f'//{token.text[2:-2]}'
                if pre_token.type not in [lexer.LINE_COMMENT, lexer.COMMENT]:
                    output_stream.write(text)
            else:
                output_stream.write(text)
            if token.type != 108:  # check if not \n
                pre_token = token
            token = lexer.nextToken()
        output_stream.close()

        output_stream = open(r"" + out_path, "r")
        print(*output_stream.readlines())
        output_stream.close()


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Java Refactor Comments')
    arg_parser.add_argument(
        '-n', '--file',
        help='input java file path',
        default=r"Game.java"
    )
    arg_parser.add_argument(
        '-out', '--out',
        help='output java file path',
        default=r"GameRefactored.java"
    )
    args = arg_parser.parse_args()
    refactor(args.file, args.out)