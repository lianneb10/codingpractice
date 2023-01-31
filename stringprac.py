slang ='''

Glow-up: Think of this term as a way of describing how someone improved from where they used to be.
Slay: This word means to do something well or to do a good job.
Bet: Bet is a way of saying “yes” or “OK” or “it's on.”
Vibing: Gen Z is big on vibes. Vibing describes a generic positive feeling that someone has about something.
Stan: This word is synonymous with supporting something.
Sus: Short-hand for suspicious.
Yeet: To throw.

'''

solo=slang.strip().split('\n')[0]


lineArray=slang.strip().split('\n')
for i in range(len(lineArray)) :
    line=lineArray[i]
    # print(line.split(':')[0])


# sentence = "I threw it out the window"

# newSentence=sentence.replace("threw","")

# print(newSentence)

sentence = "It was great that I threw the strange thing out the window for real"

sentence_replacements = [
  ["threw", "yeeted"],
  ["great", "bussin"],
  ["strange", "sus"],
  ["for real", "no cap"]
]

for i in range(len(sentence_replacements)) : 
    pair=sentence_replacements[i]
    oldWord=pair[0]
    newWord=pair[1]
    sentence = sentence.replace(oldWord, newWord)
    
print(sentence)
