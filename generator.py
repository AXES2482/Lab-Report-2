import random

articles = getWords('articles.txt')

nouns = getWords('nouns.txt')

verbs = getWords('verbs.txt')

prepositions = getWords('prepositions.txt')

def getWords(filename):
    fp = open(filename)
    temp_list = list()
    for each_line in fp:
        each_line = each_line.strip()
        temp_list.append(each_line)

    words = tuple(temp_list)
    fp.close

    return words
