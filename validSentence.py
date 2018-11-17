import re

fname = 'validSentence.txt'
fo = open(fname)
fr = fo.read()
# sentences = re.split(r"[A-Z]\w+[^A-Za-z0-9]*\s(\w*\s*)+(\.!?)*", fr)
# for lines in sentences:
#     print(lines)
for sentences in fr:
    for lines in re.findall('[A-Z]\w+[^A-Za-z0-9]*\s(\w*\s*)+(\.!?)*', sentences):
        print(lines)
