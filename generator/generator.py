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

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()
 
def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)
 
def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()
 
def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()
 
def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
 
# The entry point for program execution
if __name__ == "__main__":
    main()
