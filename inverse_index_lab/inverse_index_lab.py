from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    '''
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    '''
    #review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return ["See it!", "A gem!", "Ideological claptrap!"][randint(0,2)] #review_options[randint(1,3)]

## Tasks 2 and 3 are in dictutil.py


## Task 4    
def makeInverseIndex(strlist): 
    enumDocs = [i for i in enumerate(strlist)] # get list of lists of index and document 
    wordKeys = set(sum([d.split() for d in strlist], []))
    dictI = {key:set() for key in wordKeys}
    for doc in enumDocs:
        docSp = doc[1].split()
        for word in docSp:
            dictI[word].add(doc[0])  

    return dictI
'''
Input: a list of documents as strings

set(sum([d.split() for d in strlist], []))

Output: a dictionary that maps each word in any document to the set consisting of the
        document ids (ie, the index in the strlist) for all documents containing the word.
sum(list1,list2,list3) returns a flattened list
Note that to test your function, you are welcome to use the files stories_small.txt
  or stories_big.txt included in the download.
'''

## Task 5
def orSearch(ii, q):
    return set(sum([list(val) for (key,val) in ii.items() if key in q], []))
'''
Input: an inverse index, as created by makeInverseIndex, and a list of words to query
Output: the set of document ids that contain _any_ of the specified words
'''

## Task 6
def andSearch(ii, q):
    sets = [val for (key,val) in ii.items() if key in q]
    ints = sets[0];
    for s in sets:
        ints = ints & s 
    insect = set()
    ints2 = {insect.intersection(val) for (key, val) in ii.items() if key in q}
    return ints2
'''
Input: an inverse index, as created by makeInverseIndex, and a list of words to query
Output: the set of all document ids that contain _all_ of the specified words
'''
     
