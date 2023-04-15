#!/usr/bin/env python3

import re
from enum import Enum, auto


def give_meaning(words):
    tokens = []

    for keysId in range(len(words) - 1):
        meaning = []
        word = words[keysId]
        suffix = words[keysId + 1]

        match word:
            case 'item' | 'remember' | 'howTo':
                meaning = [suffix, word + ' declaration']
            case '"' | "'":
                meaning = [suffix, 'string']
            case _:
                meaning = [suffix, '']

        if meaning:
            tokens.append(meaning)

    return tokens




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
    file_string = file.read()
    previous_identation = 0
    identation = 0
    word = ''
    error = []
    tokens = []
    words = ['']
    words_past_counter = 0
    file_len = len(file_string) 
    analyzing = 0

    for charId in range(file_len):
        char = file_string[charId]
        operand_regex = '([!-/]|[:-?]|[\[-\^]|`|[{-~])'
        operand_regex_no_spaces = '.+([!-/]|[:-?]|[\[-\^]|`|[{-~])'
# operands
        if check_regexes([operand_regex], word):
            operand = check_regexes([operand_regex], word).group(0)[-1]
            if operand == '(' or operand == ')':
                if charId != file_len - 1:
                    operand += ' '
            words.append(operand)
            word = ''
        elif check_regexes([operand_regex_no_spaces], word):
            operand = check_regexes([operand_regex_no_spaces], word).group(0)[-1]
            words.append(word.replace(operand, ''))
            words.append(operand)
            word = ''

        if charId == 0 and char != '-':
            identation = 0
            if previous_identation > identation:
                words.append('}')
            previous_identation = identation
            previous_identation = identation
        word += char


        if char == '\n':
            # words.append('\n')
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
                words.append('}')
                # print(words[-1], 98)
            previous_identation = identation
            previous_identation = identation
            word = ''

        else:
            word = word.replace(' ', '')
            if word:
                words.append(word)
                # print(words[-1],107)

        if words_past_counter < len(words):
            word = ''

    tokens = give_meaning(words)
    # for keysId in range(len(words)):
    #     meaning = give_meaning(words, words_past_counter - 1)
    #     if meaning:
    #         tokens.append(meaning)

    print(tokens)
    print(words)
    file.close()

tokenize('prototype.bell')
