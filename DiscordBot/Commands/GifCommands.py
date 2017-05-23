import random

temp = open('Files/giflist.txt',  encoding = "utf8")
data = temp.readlines()
temp.close()

giflist = []

for line in data:
    line = line.strip().split(': ',1)
    giflist.append(line)

gifdict = {}

for entry in giflist:
    gifdict[entry[0]] = entry[1]

commandlist = [['$gif [Name]', 'search a gif by its name'],['$gr','pull a random gif'],
              ['$list','get a link to all avalible gifs']]
def gifs(message):

    if message.content == '$list' :
        return 'http://bit.do/giflist'

    if message.content == '$gr':
        return gifrandom()

    if message.content == '$help':
        return help()

    if message.content.startswith('$gif '):
        return gifsearch(message.content[5:])
#################################

def help():
    output = ""
    for entry in commandlist:
        output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
    return output

################################

def gifsearch(message):

    output = ""

    for entry in giflist:
        if message.lower().strip() in entry[0].lower() :
            output += entry[1]

    if output == "" :
        return ('Gif not found.')

    return output

################################

def gifrandom():
    return giflist[random.randint(0,len(giflist)-1)][1]
 