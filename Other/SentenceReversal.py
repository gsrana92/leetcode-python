# Reverse a sentence
# Example: input: 'This is the best'
#         output: 'best the is The'

def sentence_reversal(s):
    s = s.split()
    out = ' '
    return out.join(reversed(s))


print(sentence_reversal('This is the best'))
print(sentence_reversal('   I took a walk today  '))

def sentence_reversal2(s):
    words = []
    length = len(s)
    space = [' ']

    out = []

    i = 0

    while i < length:

        if s[i] not in space:

            word_start = i

            while i < length and s[i] not in space:
                i += 1

            words.append(s[word_start: i])

        i += 1

    print(words)

    for i in range(len(words)):
        word = words.pop()
        out.append(word)

    return ' '.join(out)


print(sentence_reversal2('  This is the best  '))

















