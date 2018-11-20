#Take data and input into variable
import re

fileName = 'validSentence.txt'
fileOpen = open(fileName)
fileRead = fileOpen.read()

#Process data and place into a different variable
list = list()
for lines in fileRead:
    list.append(re.findall('([[A-Z]\w+[^A-Za-z0-9]*\s+[\w\s]+[.!?]*)', lines))

#Print
print(list)