"""Find the shortest path from a 'beginword' to 'endword' from a given list of words.
e.g Input:
    beginword = "hit"
    endword = "cog"
    wordlist = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

    The shortest path is (one of the) hit -> hot -> dot -> dog -> cog

    Output: 5

    """
from _collections import deque

def preprocessedWords(wordList):
    d = {}
    for word in wordList:
        for letter in range(len(word)):
            wildcard = word[:letter] + '_' + word[letter + 1:]

            if wildcard not in d:
                d[wildcard] = []
            d[wildcard].append(word)

    return d


def wordLadderProblem(beginword, endWord, wordList):
    # checking errors
    if not beginword or not endWord or not wordList or not endWord in wordList:
        return 0

    # preprocessed words
    wordTree = preprocessedWords(wordList)
    print(preprocessedWords(wordList))


    #BFS
    queue = deque()
    queue.append([beginword, 1])
    visited = set()

    while queue:
        curr, level = queue.popleft()

        for i in range(len(curr)):
            wildcard = curr[:i] + '_' + curr[i+1:]

            if wildcard in wordTree:
                for word in wordTree[wildcard]:
                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited.add(word)
                        queue.append([word, level+1])

    return 0

print(wordLadderProblem('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))



