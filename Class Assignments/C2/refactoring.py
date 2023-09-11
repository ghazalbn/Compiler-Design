import argparse
import os
from antlr4 import *
from gen.JavaLexer import JavaLexer
from antlr4.TokenStreamRewriter import TokenStreamRewriter


def refactor(file_path, out_path, name, number):

    if file_path.split('.')[-1] == 'java':
        stream = FileStream(r""+file_path, encoding="utf8")

        lexer = JavaLexer(stream)

        if os.path.exists(out_path):
            os.remove(out_path)
        output_stream = open(r"" + out_path, "a")

        token = lexer.nextToken()
        while token.type != Token.EOF:
            text = token.text
            if token.type == lexer.LINE_COMMENT:
                text = f'/*{name} {number}\n{token.text[2:]}*/'

            if token.type == lexer.COMMENT:
                text = f'{token.text[:2]} {name} {number}\n{token.text[2:]}'
            output_stream.write(text)
            token = lexer.nextToken()
        output_stream.close()

        output_stream = open(r"" + out_path, "r")
        print(*output_stream.readlines())
        output_stream.close()


if __name__ == "__main__":
    name = 'FatemeZahra Bakhshande'
    number = '98522157'
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
    arg_parser.add_argument(
        '-name', '--name',
        help='your full name',
        default=name
    )
    arg_parser.add_argument(
        '-number', '--number',
        help='your student number',
        default=number
    )
    args = arg_parser.parse_args()
    refactor(args.file, args.out, args.name, args.number)



    # second approach
    # token_stream = CommonTokenStream(lexer)
    # token_stream_rewriter = TokenStreamRewriter(token_stream)
    # for token in token_stream.tokens:
    #     if token.type in [lexer.LINE_COMMENT, lexer.COMMENT]:  # Comments & Line Comments
    #         text = f'/*{name} {number}\n{token.text[2:]}*/' \
    #             if token.type == lexer.LINE_COMMENT \
    #             else f'{token.text[:2]} {name} {number}\n{token.text[2:]}'
    #
    #         token_stream_rewriter.replaceIndex(
    #             index=token.tokenIndex,
    #             text=text
    #         )
    # output_stream.write(token_stream_rewriter.getDefaultText())
    # print(token_stream_rewriter.getDefaultText())
