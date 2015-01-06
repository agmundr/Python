pyg = 'ay'
trans_text = "Translation: "

print "Pig Latin Translator v1.0"

original = raw_input('Enter a word:') #User to enter a word

if len(original) > 0 and original.isalpha(): #check for non alpha chars
    word = original.lower() #converts to lower case
    first = original[0].lower() #grabs first char for translation
    new_word = trans_text + word[1:len(word)] + first + pyg #Removes and Moves first letter or input word and adds ay to the end for translation
    print new_word
else:
    print 'empty' #printed if nothing or non alpha chars used
