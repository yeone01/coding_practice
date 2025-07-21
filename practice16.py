line = "Bravely bold Sir Robin rode forth from Camelot\
Yes, brave Sir Robin turned about\
He was not afraid to die, O brave Sir Robin\
And gallantly he chickened out\
He was not at all afraid to be killed in nasty ways\
Bravely talking to his feet\
Brave, brave, brave, brave Sir Robin\
He beat a very brave retreat"

s = line.split("\n")
s = s[1 : len(s) : 2]
s = "\n".join(s)


print(s)
