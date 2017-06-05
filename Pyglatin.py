pyg = 'ay'

print 'Welcome to the pig Latin Translator'

original = raw_input("Enter a word:   ")
word = original.lower()
first = word[0]
new_word = word[1:] + first + pyg
if len(original) > 0 and original.isalpha() == True:
    print new_word
else:
    print "Empty"
