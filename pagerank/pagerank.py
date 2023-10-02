import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    choice = random.random()
    if(choice < damping_factor):
        return random.choice(list(corpus[page]))
    else:
        return random.choice(list(corpus.keys()))
    #raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    dictionary  = dict()
    for item in list(corpus.keys()):
        dictionary[item] = 0
    
    page = random.choice(list(corpus.keys()))

    for i in range(n):
        page = transition_model(corpus, page, damping_factor)
        dictionary[page] = 1 + dictionary[page]

    for item in list(corpus.keys()):
        dictionary[item] = dictionary[item]/n

    return dictionary

    #raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    ranks = dict()
    for item in list(corpus.keys()):
        ranks[item] = 1/len(list(corpus.keys()))

    reverseCorpus = dict()
    for it in list(corpus.keys()):
        links = set()
        for item in list(corpus.keys()):
            if(it in list(corpus[item])):
                links.add(item)
        reverseCorpus[it] = links

    temp = dict()
    unfinished = True
    while(unfinished):
        unfinished = False
        for item in list(corpus.keys()):
            i = iterate(corpus, damping_factor, item, ranks, reverseCorpus)
            #print(ranks[item])
            #print(i)
            if not ((ranks[item]<(i+0.001)) and (ranks[item]>(i-0.001))):
                unfinished = True
            temp[item] = i
        ranks = temp
        if(not unfinished):
            return normalize(ranks)

def normalize(ranks):
    summ = 0
    for i in ranks:
        summ+=ranks[i]
    divisor = 1/summ
    for i in ranks:
        ranks[i]=round(ranks[i]*divisor,4)
    return ranks

    #raise NotImplementedError

def iterate(corpus, damping_factor, page, ranks, reverseCorpus):
    toReturn = (1-damping_factor)/len(list(corpus.keys()))
    toAdd = 0
    for item in list(reverseCorpus[page]):
        toAdd += ranks[item]/len(corpus[item])
    return toReturn + (damping_factor*toAdd)

if __name__ == "__main__":
    main()
