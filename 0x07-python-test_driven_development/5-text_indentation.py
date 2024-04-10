#!/usr/bin/python3
def text_indentation(text):
    '''a function that prints a text with 2 new lines after
    each of these characters: ., ? and :'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while (i < len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
            i += 2
        else:
            print(text[i], end="")
            i +=1
