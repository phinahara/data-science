def makeInverseIndex(L):
    dictionary = dict()
    for (i,st) in enumerate(L):
        words = {word:i for word in st.split()}
        for w in words:
            if w not in dictionary:
                dictionary[w]={i}
            else:
                dictionary[w].add(i)
    return dictionary

def orSearch(inverseIndex, query):
    result = set()
    for word in query:
        result = result|inverseIndex[word]
    return result

def andSearch(inverseIndex, query):
    result = set()
    for word in query:
        if len(result) == 0:
            result=inverseIndex[word]
        else:
            result = result&inverseIndex[word]
    return result