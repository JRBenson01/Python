def censor(text, word):
    words = text.split()
    length = len(word)
    joined_text = []
    d = " "
    for i in words:
        if i == word:
            joined_text.append("*"*length)
        else:
            joined_text.append(i)
    print joined_text
    print "joining..."
    print d.join(joined_text)
censor("hey hey hey", "hey")
