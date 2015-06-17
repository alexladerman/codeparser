'''
Created on 5 Apr 2013

@author: Alex
'''
import sys
import re


elem_delimiters = "\n;, "
block_delimiters = (('(',')'),('[',']'),('{','}'))    

def parseCodeFile(filepath):
    tree = list()
    codefile = open(filepath)
    append_str(tree, codefile.read())
    for bd in block_delimiters[:1]:
        for i,e in enumerate(tree):
            tree[i] = parse_block(e, bd)[0]
    print(tree)
    for sep in elem_delimiters:
        tree = split_block(tree, sep)
    print(tree)
    print_tree(tree,0)

def split_block(l, sep):
    for i,e in enumerate(l):
        if isinstance(e, str):
            e = e.split(sep)
            if len(e) > 1:
                l[i] = e
        else:
            e = split_block(e, sep)
            if len(e) > 1:
                l[i] = e
    return l
    
def parse_block(code, bd):
    s = ""
    l = []
    i = 0
    while i < len(code):
        c = code[i]
        if c == bd[0]:
            append_str(l, s)
            s = ""
            sll = parse_block(code[i+1:], bd)
            l.append(sll[0])
            i += sll[1]
        elif c == bd[1]:
            append_str(l,s)
            return (l,i+1)
        else:
            s += c
        i += 1
    append_str(l, s)
    return (l,len(code))


def proper_split(e, sep):
    words = e.split(sep)
    for i,word in enumerate(words):
        word = word.strip()
        if word == "" :
            del words[i]
    return words

def proper_strip(s):  
    s = re.sub(r"(?m)^[^\S\n]+", "", s)
    return s
 
def append_str(l, s):
    if (len(s) > 0):
        elem_delims = "\n;, "
        for sep in elem_delims:
            ll = s.split(sep)
            if len(ll) > 1:
                for e in ll:
                    l.append(proper_strip(e))
                return
        l.append(proper_strip(s))
        
def get_separator(l):
    elem_delims = "\n;, "
    for sep in elem_delims:
        for e in l:
            if isinstance(e,str):
                if e.find(sep) >= 0:
                    return sep
    return '\0'

def split_list(l):
    c = get_separator(l)
    if c != '\0':
        
            
#         sys.stdout.write(c)

def print_tree(tree, depth):
    print(' '*depth, '{')
    depth += 3
    for node in tree:
        if isinstance(node, str):
            print(' '*depth, node )
        else:
            print_tree(node, depth)
    depth -= 3
    print(' '*depth, '}')
    
parseCodeFile("codefile.txt")


