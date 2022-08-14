import sys

print(sys.version)
print(sys.argv)
myfile = open('test.txt')
#print(myfile.read())
sentence = 'this is a test file to count the number of certain words in a text file. The fuck is the'


def countWord(myfile, s):
    file = myfile.read()
    myfile.close()
    print('-->',myfile)

    count = 0

    for word in list(file.split(' ')):
        if word == s:
            count += 1


    return count


def reverse(s):
    if len(s) == 1:
        return s

    for i in range(len(s)):



print(countWord(myfile, 'the'))
