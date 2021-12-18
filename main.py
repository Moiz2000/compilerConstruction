from regex import *
import wordSpilitter
import SyntaxAnalyzer


Tokens = wordSpilitter.wordCount("words.txt")
# print(Tokens)

SyntaxAnalyzer.Syntax_Analyzer(Tokens)
