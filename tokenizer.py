'''
Created on 6 Apr 2013

@author: Alex
'''
import re

elem_delimiters = "\n;, "
block_delimiters = (('(',')'),('[',']'),('{','}'))   
block_delimiters_array = "{}[]()" 
#bd = "([\{\}\[\]\(\)\n;,\s\+{ 1,2}])"
sep = "([^a-zA-Z0-9][\+(?!+)])"

def parseCodeFile(filepath):
    tree = list()
    codefile = open(filepath)
    code = codefile.read()
    code = code.replace('('," ( ").replace(')', " ) ")
    print(re.split(sep, code))
    


parseCodeFile("codefile.txt")
