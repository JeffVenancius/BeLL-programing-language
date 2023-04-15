#!/usr/bin/env python3

import re
from enum import Enum, auto

# # based on gdscript
# class Token(Enum):
#     EMPTY = auto()
#     ANNOTATION = auto() 
#     IDENTIFIER = auto() 
#     LITERAL = auto() 
#     LESS = auto() 
#     LESS_EQUAL = auto() 
#     GREATER = auto() 
#     GREATER_EQUAL = auto() 
#     EQUAL_EQUAL = auto() 
#     IS_EQUAL = auto() 
#     BANG_EQUAL = auto() 
#     IS_NOT_EQUAL = auto() 
#     AND = auto() 
#     OR = auto() 
#     NOT = auto() 
#     XOR = auto() 
#     AMPERSAND_AMPERSAND = auto() 
#     PIPE_PIPE = auto() 
#     BANG = auto() 
#     AMPERSAND = auto() 
#     PIPE = auto() 
#     TILDE = auto() 
#     CARET = auto() 
#     LESS_LESS = auto() 
#     GREATER_GREATER = auto() 
#     PLUS = auto() 
#     MINUS = auto() 
#     STAR = auto() 
#     STAR_STAR = auto() 
#     SLASH = auto() 
#     PERCENT = auto() 
#     EQUAL = auto() 
#     PLUS_EQUAL = auto() 
#     MINUS_EQUAL = auto() 
#     STAR_EQUAL = auto() 
#     STAR_STAR_EQUAL = auto() 
#     SLASH_EQUAL = auto() 
#     PERCENT_EQUAL = auto() 
#     LESS_LESS_EQUAL = auto() 
    # GREATER_GREATER_EQUAL = auto() 
    # AMPERSAND_EQUAL = auto() 
    # PIPE_EQUAL = auto() 
    # CARET_EQUAL = auto() 
    # IF = auto() 
    # ELIF = auto() 
    # ELSE = auto() 
    # FOR = auto() 
    # WHILE = auto() 
    # BREAK = auto() 
    # CONTINUE = auto() 
    # SKIP = auto() 
    # GO_TO = auto() 
    # BY = auto() 
    # PASS = auto() 
    # RETURN = auto() 
    # MATCH = auto() 
    # AS = auto() 
    # ASSERT = auto() 
    # AWAIT = auto() 
    # BREAKPOINT = auto() 
    # CLASS = auto() 
    # CLASS_NAME = auto() 
    # CONST = auto() 
    # ENUM = auto() 
    # EXTENDS = auto() 
    # FUNC = auto() 
    # IN = auto() 
    # IS = auto() 
    # NAMESPACE = auto() 
    # PRELOAD = auto() 
    # SELF = auto() 
    # SIGNAL = auto() 
    # STATIC = auto() 
    # SUPER = auto() 
    # TRAIT = auto() 
    # VAR = auto() 
    # VOID = auto() 
    # BRACKET_OPEN = auto() 
    # BRACKET_CLOSE = auto() 
    # BRACE_OPEN = auto() 
    # BRACE_CLOSE = auto() 
    # PARENTHESIS_OPEN = auto() 
    # PARENTHESIS_CLOSE = auto() 
    # COMMA = auto() 
    # SEMICOLON = auto() 
    # PERIOD = auto() 
    # PERIOD_PERIOD = auto() 
    # COLON = auto() 
    # DOLLAR = auto() 
    # FORWARD_ARROW = auto() 
    # UNDERSCORE = auto() 
    # NEWLINE = auto() 
    # INDENT = auto() 
    # DEDENT = auto() 
    # CONST_PI = auto() 
    # CONST_TAU = auto() 
    # CONST_INF = auto() 
    # CONST_NAN = auto() 
    # VCS_CONFLICT_MARKER = auto() 
    # BACKTICK = auto() 
    # QUESTION_MARK = auto() 
    # ERROR = auto() 
    # TK_EOF = auto() 
    # TK_MAX = auto() 

# tokenNames = [
	# "Empty", # EMPTY, ?
	# # Basic
	# "Annotation", # ANNOTATION ?
	# "Identifier", # IDENTIFIER, ?
	# "Literal", # LITERAL, ?
	# # Comparison
	# "<", # LESS,
	# "<=", # LESS_EQUAL,
	# ">", # GREATER,
	# ">=", # GREATER_EQUAL,
	# "==", # EQUAL_EQUAL,
	# "is a" # EQUAL_EQUAL,
	# "!=", # BANG_EQUAL,
	# "is not a" # BANG_EQUAL,
	# # Logical
	# "and", # AND,
	# "or", # OR,
	# "not", # NOT,
	# "but", # XOR,
	# "&&", # AMPERSAND_AMPERSAND,
	# "||", # PIPE_PIPE,
	# "!", # BANG,
	# # Bitwise
	# "&", # AMPERSAND,
	# "|", # PIPE,
	# "~", # TILDE,
	# "^", # CARET,
	# "<<", # LESS_LESS,
	# ">>", # GREATER_GREATER,
	# # Math
	# "+", # PLUS,
	# "-", # MINUS,
	# "*", # STAR,
	# "**", # STAR_STAR,
	# "/", # SLASH,
	# "%", # PERCENT,
	# # Assignment
	# "=", # EQUAL,
	# "+=", # PLUS_EQUAL,
	# "-=", # MINUS_EQUAL,
	# "*=", # STAR_EQUAL,
	# "**=", # STAR_STAR_EQUAL,
	# "/=", # SLASH_EQUAL,
	# "%=", # PERCENT_EQUAL,
	# "<<=", # LESS_LESS_EQUAL,
	# ">>=", # GREATER_GREATER_EQUAL,
	# "&=", # AMPERSAND_EQUAL,
	# "|=", # PIPE_EQUAL,
	# "^=", # CARET_EQUAL,
	# # Control flow
	# "is", # IF,
	# "then is", # ELIF,
    # "well then", # ELSE,
	# "do", # FOR,
	# "as long", # WHILE,
	# "cut", # BREAK,
	# "keep going", # CONTINUE,
	# "skip", # SKIP,
    # "go to" # GO_TO (example: go to function with args by n lines, based on BASIC but relative, with this you can start a function in the middle)
    # "by", # BY
	# "ignore", # PASS,
	# "get", # RETURN,
	# "what is", # MATCH,
	# # Keywords
	# "as", # AS,
	# "check", # ASSERT,
	# "wait for", # AWAIT,
	# "breakpoint", # BREAKPOINT,
	# "kind", # CLASS,
	# "name", # CLASS_NAME,
	# "remember", # CONST,
	# "cards", # ENUM,
	# "inherits", # EXTENDS,
	# "howTo", # FUNC,
	# "in", # IN,
	# "is", # IS,
	# "family", # NAMESPACE
	# "preload", # PRELOAD,
	# "self", # SELF,
	# "signal", # SIGNAL,
	# "common knowledge", # STATIC (don't know yet),
	# "genus", # SUPER,
	# "trait", # TRAIT,
	# "item", # VAR,
	# "void", # VOID,
	# # Punctuation
	# "[", # BRACKET_OPEN,
	# "]", # BRACKET_CLOSE,
	# "{", # BRACE_OPEN,
	# "}", # BRACE_CLOSE,
	# "(", # PARENTHESIS_OPEN,
	# ")", # PARENTHESIS_CLOSE,
	# ",", # COMMA,
	# ";", # SEMICOLON,
	# ".", # PERIOD,
	# "..", # PERIOD_PERIOD,
	# ":", # COLON,
	# "$", # DOLLAR,
	# "->", # FORWARD_ARROW,
	# "_", # UNDERSCORE,
	# # Whitespace
	# "Newline", # NEWLINE,
	# "Indent", # INDENT (- ),
	# "Dedent", # DEDENT,
	# # Constants
	# "PI", # CONST_PI,
	# "TAU", # CONST_TAU,
	# "INF", # CONST_INF,
	# "NaN", # CONST_NAN,
	# # Error message improvement
	# "VCS conflict marker", # VCS_CONFLICT_MARKER,
	# "`", # BACKTICK,
	# "?", # QUESTION_MARK,
	# # Special
	# "Error", # ERROR,
	# "End of file", # EOF,
    # ]

def check_regexes(regexes, word):
    for regex in regexes:
        matched = pattern.match("/" + regexes + "/g", word)
        if matched:
            return matched
    return None
    

def get_regexes(char, past_token):
    regexes = []

    match char:
        case ':':
            regexes.append('(^[^ -,\.-@])+[_A-Za-z]:') # START(any char that is not a symbol or letter except for - and _)(any letter, number, _):END
        case ')':
            regexes.append('\({2}[\s\S]*\){2}') # START((ANYTHING))END
        case 'i':
            regexes.append('item |inherits')
        case 'r':
            regexes.append('remember')

    if past_token != '}':
        match char:
            case 'c':
                regexes.append('create signal to |common knowledge ')
            case 'f':
                regexes.append('family ')
            case 'h':
                regexes.append('howTo ')
            case 'k':
                regexes.append('kind ')
            case 'n':
                regexes.append('name ')
   else:
       match char:
           case ' ':
                regexes.append(' +(-|\+|\+-|>{1,2}|<{1,2}|\*{1,2}|\|{1,2}|\&{1,2}|=|%|~|\^|\/) +') # (space = at least 1)START - OR + OR +- OR > OR >> OR < OR << OR * OR ** OR | OR || OR & OR && OR = OR % OR ~ OR ^ OR / END
                regexes.append(' +(--|\+\+)') # (space = at least 1)START --OR++END
                regexes.append(' +(-|\+|=|>{1,2}|<{1,2}|\*{1,2}|\||\&|%|!|/)= +') # (space = at least 1)START -= OR += OR == OR >= OR >>= OR <= OR <<= OR *= OR **= OR |= OR &= OR %= OR != OR /= END
                regexes.append(' +(a|but|and|or|by|in|with|is a|is not a|in|as) +') # (space = at least 1)START a OR but OR and OR or OR by OR in OR with OR is a OR is not a OR in OR as END
            case '?':
                regexes.append('\?{1,2}') # START?OR??END
            case '-':
                regexes.append('-+ ') # (- = at least 1)START- END
            case 'a':
                regexes.append('as long ')
            case 'c':
                regexes.append('cut\n')
            case 'd':
                regexes.append('do in ')
            case 'g':
                regexes.append('go to |get ?\n')
            case 'i':
                regexes.append('item |ignore\n')
            case 'n':
                regexes.append('nothing\n')
            case 'r':
                regexes.append('remember ')
            case 's':
                regexes.append('skip\n')
            case 't':
                regexes.append('then is ')
            case 'w':
                regexes.append('well then: |what is ')
    return regexes

def is_a_coment(word):
    return check_regexes('\({2}[\s\S]*', word) # START((ANYTHINGEND

def comment_is_finished(word):
    return check_regexes('[\({2}[\s\S]*\){2}]', word)

def should_ident(previous_identation, identation):
    return previous_identation > identation:


def bad_idented_calculation(word):
    regexes = []
    regexes.append('[_A-Za-z]+(-{1,2}|\+{1,2}|\+-|>{1,2}|<{1,2}|\*{1,2}|\|{1,2}|\&{1,2}|=|%|~|\^|\/)') # START-OR+OR+-OR>OR>>OR<OR<<OR*OR**OR|OR||OR&OR&&OR=OR%OR~OR^OR/END
    return check_regexes(regexes, word()

def tokenize(source):
    file = open(source, 'r')
    lines = (file.readlines())
    previous_identation = 0
    identation = 0
    word = ''
    error = []
    tokens = []
    tokens_past_counter = 0

    for lineId in range(len(lines)):
        line = lines[lineId]
        for charId in range(len(line)):
            char = line[charId]
            if not word:
                word = char

            if is_a_comment(word):
                if comment_is_finished(word)
                    word = ''
                else:
                    word += char
                continue

            regexes = get_regexes(word[0], tokens[-1])
            valid_regex = check_regexes(regexes, word) 

            if valid_regex:
                if word[0] == '-':
                    identation = word.count('-')
                    if should_ident(previous_identation, identation):
                        tokens.append('}')
                        word = ''
                    previous_identation = identation
                    continue

                if ' ' in word:
                    tokens.append(word.replace(' ', ''))
                    tokens.append(' ')
                else:
                    if bad_idented_calculation(word):
                         tokens.append(word)
                        pass
                    tokens.append(word)
            else:
                regexes = get_regexes(word[-1], tokens[-1])
                checked = check_regexes(regexes, word) 

                if checked:
                    if word[-1] == ':':
                        tokens.append('{')

            if tokens_past_counter < len(tokens):
                word = ''
            tokens_past_counter = len(tokens)

            word += char

    file.close()



tokenize('prototype.bell')



















# binary_comparison = "/(.)+ +(<|<=|<<|>|>=|>>|=|==|\+|\+=|-|-=|\/|\/=|%|%=|&|&&|\||\|{2}|~|\^|\*|\*=|\*{2}|\*{2}=|and|or|not|but|with|is a|as|) +(.)/g"
# identation = "/(-)* /g"



# is_idented = "?<=- |)" # - statement, statement 
# item_name = "([A-Za-z-_]\d*)" # item123_-
# duck_item_assigment = is_idented + item_name
# # duck_item = '/' + is_idented + item_name + '/g'

# assignment = "/\S+ +\S* :/g"

# is_definable = '([A-Za-z])+ \g'
# definition = '/' + is_idented + is_definable
# definition_not_identable = '/^' + is_definable # howTo

# # remember = "/(?<=- )remember |^remember /g"
# # less = any1 + "<" + any2
# # less_equal = "/ <= /g"
# # greater = "/ > /g"
# # greater_equal = "/ >= /g"
# # equal_equal = "/ == /g"
# # not_equal = "/ != /g"
# # double_ampersand = "/ && /g"
# # double_pipe = "/ || /g"
# # bang = "/ ! /g"
# is_a =  "/ is a /g"
# is_not_a =  "/ is not a /g"
# _and = "/ and /g"
# _or = "/ or /g"
# _not = "/ not /g"
# but = "/ but /g"
# two_dots ='/:/g'
# _with = '/ with /g'
# end_dot = '/.\./g'
# comment = '/\({2}.*\){2}$/g'
# multiline_comment = '/\({2}.*[^\){2}]$/g'
