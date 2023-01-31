"""
A sentence is made up of a group of words.
Each word is a sequence of letters, ('a'z; 'A'
'Z'), that may contain one or more hyphens and
may end in a punctuation mark: period (.), comma G),
question mark (?), or exclamation point (!). Words
will be separated by one or more white space
characters.Hyphens join two words into
one and should he retained while the other
punctuation marks should be stripped.
Determine the number of words in a given
sentence.
"""

one="How many eggs are in a half-dozen, 13?"
# Should have 7 words

two="he is a good programmer, he won 865 competitions, but sometimes he dont. What do you think? All test-cases should pass. Done-done?"
# Should have 21 words

# print(len(one))
# print(len(two))

def wordCount(x):
    print(x)
    
wordCount("Hi I'm a sentence")