import nltk
import sys
import os
import string
import numpy

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    dictionary  = dict()
    for files in os.listdir(directory):
        with open(os.path.join(directory, files), 'r') as f:
            txt = f.read()
            dictionary[files] = txt

    return dictionary

    #raise NotImplementedError


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    doc = document.lower()
    #print(string.punctuation)
    docEdit = ""
    for char in doc:
        if not(char in string.punctuation):
            docEdit += char
        else:
            docEdit += " "
    ls = nltk.word_tokenize(docEdit)
    toRet = list()
    for i in ls:
        if not(i in nltk.corpus.stopwords.words("english")):
            toRet.append(i)
    return toRet

    #raise NotImplementedError


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    dictionary = dict()
    for doc in list(documents.keys()):
        sett = set(documents[doc])
        for word in sett:
            #print(word)
            if not(word in list(dictionary.keys())):
                dictionary[word.lower()] = 0
            dictionary[word.lower()] += 1

    for val in list(dictionary.keys()):
        if(dictionary[val] != 0):
            dictionary[val] = numpy.log(len(documents.keys())/dictionary[val])

    #print(dictionary.keys())
    return dictionary
    #raise NotImplementedError


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    q = query
    dictionary = dict()
    for word in q:
        w = word.lower()
        if(w in list(idfs.keys())):
            idf = idfs[w]
            if(idf!=0):
                for f in list(files.keys()):
                    tf = files[f].count(w)
                    if not(f in list(dictionary.keys())):
                        dictionary[f] = 0
                    dictionary[f] += (tf*idf)
        else:
            dictionary[f] = 0
    
    toReturn = list()
    for i in range(n):
        max = 0
        toRemove = None
        for f in list(dictionary.keys()):
            #print(dictionary[f])
            if(dictionary[f]>max):
                max=dictionary[f]
                toRemove = f
        toReturn.append(toRemove)
        dictionary.pop(toRemove)

    return toReturn

    #raise NotImplementedError


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """

    dictionary = dict()
    q = query
    for word in q:
        w = word.lower()
        if(w in list(idfs.keys())):
            idf = idfs[w]
            #print(w)
            #print(idf)
            if(idf!=0):
                for f in list(sentences.keys()):
                    if not(f in list(dictionary.keys())):
                        dictionary[f] = 0
                    if(w in sentences[f]):
                        dictionary[f] += (idf)
        else:
            dictionary[f] = 0

    toReturn = list()
    for i in range(n):
        max = 0
        toRemove = None
        for f in list(dictionary.keys()):
            if(dictionary[f]==max):
                if(toRemove!=None):
                    qtd1 = 0
                    qtd2 = 0
                    for word in query:
                        for w in sentences[f]:
                            if(word==w.lower()):
                                qtd1 += 1
                        for w in sentences[toRemove]:
                            if(word==w.lower()):
                                qtd2 += 1
                    qtd1 = qtd1/len(sentences[f])
                    qtd2 = qtd2/len(sentences[toRemove])
                    if(qtd1>qtd2):
                        toRemove = f
                else:
                    toRemove = f
            if(dictionary[f]>max):
                #print(max)
                max=dictionary[f]
                toRemove = f
                #print(toRemove)
        toReturn.append(toRemove)
        dictionary.pop(toRemove)

    return toReturn

    #raise NotImplementedError


if __name__ == "__main__":
    main()
