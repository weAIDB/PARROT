# Generated from sql/hive/v3/HintParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HintParser import HintParser
else:
    from HintParser import HintParser

# This class defines a complete listener for a parse tree produced by HintParser.
class HintParserListener(ParseTreeListener):

    # Enter a parse tree produced by HintParser#hint.
    def enterHint(self, ctx:HintParser.HintContext):
        pass

    # Exit a parse tree produced by HintParser#hint.
    def exitHint(self, ctx:HintParser.HintContext):
        pass


    # Enter a parse tree produced by HintParser#hintList.
    def enterHintList(self, ctx:HintParser.HintListContext):
        pass

    # Exit a parse tree produced by HintParser#hintList.
    def exitHintList(self, ctx:HintParser.HintListContext):
        pass


    # Enter a parse tree produced by HintParser#hintItem.
    def enterHintItem(self, ctx:HintParser.HintItemContext):
        pass

    # Exit a parse tree produced by HintParser#hintItem.
    def exitHintItem(self, ctx:HintParser.HintItemContext):
        pass


    # Enter a parse tree produced by HintParser#hintName.
    def enterHintName(self, ctx:HintParser.HintNameContext):
        pass

    # Exit a parse tree produced by HintParser#hintName.
    def exitHintName(self, ctx:HintParser.HintNameContext):
        pass


    # Enter a parse tree produced by HintParser#hintArgs.
    def enterHintArgs(self, ctx:HintParser.HintArgsContext):
        pass

    # Exit a parse tree produced by HintParser#hintArgs.
    def exitHintArgs(self, ctx:HintParser.HintArgsContext):
        pass


    # Enter a parse tree produced by HintParser#hintArgName.
    def enterHintArgName(self, ctx:HintParser.HintArgNameContext):
        pass

    # Exit a parse tree produced by HintParser#hintArgName.
    def exitHintArgName(self, ctx:HintParser.HintArgNameContext):
        pass



del HintParser