#!/usr/bin/env python3

import re
from enum import Enum, auto


def check_regexes(regexes, word):
    for pattern in regexes:
        result = re.compile(pattern)
        matched = result.match(word)
        if matched:
            return matched
    return None

def is_only_spaces(word):
    return word.count(' ') == len(word)

def tokenize(source):
    file = open(source, 'r')
    lines = (file.readlines())
    previous_identation = 0
    identation = 0
    word = ''
    error = []
    tokens = ['']
    tokens_past_counter = 0

    for lineId in range(len(lines)):
        line = lines[lineId]
        line_len = len(line)
        for charId in range(line_len):
            char = line[charId]
            operand_regex = '([!-/]|[:-?]|[\[-\^]|`|[{-~])'
            operand_regex_no_spaces = '.+([!-/]|[:-?]|[\[-\^]|`|[{-~])'

# operands
            if check_regexes([operand_regex], word):
                operand = check_regexes([operand_regex], word).group(0)[-1]
                tokens.append(operand)
                word = ''
            elif check_regexes([operand_regex_no_spaces], word):
                operand = check_regexes([operand_regex_no_spaces], word).group(0)[-1]
                tokens.append(word.replace(operand, ''))
                tokens.append(operand)
                word = ''

            if charId == 0 and char != '-':
                identation = 0
                if previous_identation > identation:
                    tokens.append('}')
                previous_identation = identation
                previous_identation = identation
            word += char



            if char == '\n':
                tokens.append('\n')
                char = ' '
                word = word.replace('\n', ' ')
            elif char == '\t':
                char = ' '
                word = word.replace('\t', ' ')

            if not ' ' in word:
                continue


            identation_regex = '-+ '

# identation

            if check_regexes([identation_regex], word):
                identation = word.count('-')
                if previous_identation > identation:
                    tokens.append('}')
                previous_identation = identation
                previous_identation = identation
                word = ''

            else:
                tokens.append(word.replace(' ',''))

            if tokens_past_counter < len(tokens):
                word = ''
                tokens_past_counter = len(tokens)

    tokens = list(filter(lambda x: x != '', tokens))
    print(tokens)
    file.close()

tokenize('prototype.bell')
